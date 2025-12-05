# Milestone 1 Prototype – Olympics Data Project
# Angel Suleiman
# Ashish Solanki

import csv

def writeOutputFiles():
    # 1. new_olympic_athlete_bio.csv
    open('new_olympic_athlete_bio.csv', 'w').close()

    # 2. new_olympic_athlete_event_results.csv (adds 'age' column)
    with open('new_olympic_athlete_event_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["athlete_id", "event", "result", "age"])

    # 3. new_olympics_country.csv
    open('new_olympics_country.csv', 'w').close()

    # 4. new_olympics_games.csv
    open('new_olympics_games.csv', 'w').close()

    # 5. new_medal_tally.csv
    with open('new_medal_tally.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "edition", "edition_id", "Country", "NOC",
            "number_of_athletes", "gold_medal_count",
            "silver_medal_count", "bronze_medal_count", "total_medals"
        ])
def read_csv_dicts(filename):
    """Read a CSV file into a list of dicts. Return [] if missing or empty."""
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if not rows:
                print(f"⚠️ {filename} is empty — skipped.")
            else:
                print(f"Loaded {filename} ({len(rows)} rows)")
            return rows
    except FileNotFoundError:
        print(f"⚠️ Missing file: {filename}")
        return []
    except Exception as e:
        print(f"⚠️ Error reading {filename}: {e}")
        return []


def get_first(row, keys):
    """Return the first non-empty value among the given possible column names."""
    for k in keys:
        if k in row:
            val = str(row[k]).strip()
            if val:
                return val
    return ""

# ----------------- MILESTONE 2 STARTS HERE -----------------

import csv
import time



def load_countries(filename):
    """
    Load countries from olympics_country.csv
    into a dict: NOC -> Country name.
    """
    rows = read_csv_dicts(filename)
    noc_to_country = {}
    for r in rows:
        noc = get_first(r, ["NOC", "noc"])
        country = get_first(r, ["Country", "country", "country_name"])
        if noc:
            noc_to_country[noc] = country
    return noc_to_country


def load_games(filename):
    """
    Load games from olympics_games.csv
    into a dict: edition_id -> edition name.
    """
    rows = read_csv_dicts(filename)
    games_by_id = {}
    for r in rows:
        edition_id = get_first(r, ["edition_id", "Edition_ID", "edition id"])
        edition_name = get_first(r, ["edition", "Edition", "games"])
        if edition_id:
            games_by_id[edition_id] = edition_name
    return games_by_id



def load_event_results(event_files):
    """
    Load and combine event results from a list of CSV files.
    Returns one big list of dict rows.
    """
    all_rows = []
    for fn in event_files:
        rows = read_csv_dicts(fn)
        all_rows.extend(rows)
    print(f"✅ Combined event results rows: {len(all_rows)}")
    return all_rows



def build_medal_tally(events_rows, noc_to_country, games_by_id):
    """
    Build medal tally grouped by (edition_id, NOC).

    For each (edition_id, NOC) pair we track:
      - edition name
      - country name
      - set of unique athlete IDs
      - gold/silver/bronze counts
    """
    medal_tally = {}

    for row in events_rows:
        # Flexible column names in case files differ
        edition_id = get_first(row, ["edition_id", "Edition_ID", "edition id"])
        noc = get_first(row, ["NOC", "noc", "Team_NOC"])
        athlete_id = get_first(row, ["athlete_id", "Athlete_ID"])
        medal = get_first(row, ["medal", "Medal", "medal_type"])

        if not edition_id or not noc:
            # Can't group without these
            continue

        key = (edition_id, noc)

        if key not in medal_tally:
            medal_tally[key] = {
                "edition": games_by_id.get(edition_id, ""),
                "edition_id": edition_id,
                "Country": noc_to_country.get(noc, ""),
                "NOC": noc,
                "athletes": set(),
                "gold": 0,
                "silver": 0,
                "bronze": 0,
            }

        if athlete_id:
            medal_tally[key]["athletes"].add(athlete_id)

        m = medal.lower()
        if m == "gold":
            medal_tally[key]["gold"] += 1
        elif m == "silver":
            medal_tally[key]["silver"] += 1
        elif m == "bronze":
            medal_tally[key]["bronze"] += 1
        # any other medal value (empty, "na", etc.) is ignored

    return medal_tally

def medal_tally_to_rows(medal_tally):
    """Convert the medal_tally dict into a list of row dicts for CSV writing."""
    rows = []
    for (edition_id, noc), info in medal_tally.items():
        num_athletes = len(info["athletes"])
        total_medals = info["gold"] + info["silver"] + info["bronze"]
        row = {
            "edition": info["edition"],
            "edition_id": info["edition_id"],
            "Country": info["Country"],
            "NOC": info["NOC"],
            "number_of_athletes": num_athletes,
            "gold_medal_count": info["gold"],
            "silver_medal_count": info["silver"],
            "bronze_medal_count": info["bronze"],
            "total_medals": total_medals,
        }
        rows.append(row)

    # Sort nicely: by edition then NOC
    rows.sort(key=lambda r: (r["edition_id"], r["NOC"]))
    return rows


def write_medal_tally(filename, rows):
    """Write new_medal_tally.csv with correct header order."""
    header = [
        "edition",
        "edition_id",
        "Country",
        "NOC",
        "number_of_athletes",
        "gold_medal_count",
        "silver_medal_count",
        "bronze_medal_count",
        "total_medals",
    ]
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
    print(f"✅ Saved {filename}")



def main():
    print("🏁 Running Olympics data project ...\n")
    start = time.time()

    # Step 1: Milestone 1 – create initial output files & headers
    writeOutputFiles()

    # Step 2: Load supporting data for countries and games
    noc_to_country = load_countries("new_olympics_country.csv")
    games_by_id = load_games("new_olympics_games.csv")

    event_files = [
        "new_olympic_athlete_event_results.csv",
        "paris_medallists.csv"
    ]

    events_rows = load_event_results(event_files)

    # Step 4: Build medal tally (YOUR logic)
    medal_tally = build_medal_tally(events_rows, noc_to_country, games_by_id)
    medal_rows = medal_tally_to_rows(medal_tally)

    # Step 5: Write new_medal_tally.csv
    write_medal_tally("new_medal_tally.csv", medal_rows)

    total = time.time() - start
    print(f"\n✅ Total runtime: {total:.2f}s")
    print("🎯 Program completed successfully!")

if __name__ == "__main__":
    main()
