# Milestone 1 Prototype – Olympics Data Project
# by Angel Suleiman

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



def generate_medal_tally(df):
    """Generate medal summary and export CSV"""
    if 'noc' not in df.columns or 'medal' not in df.columns:
        print("⚠️ Medal or NOC column missing.")
        return
    tally = df.groupby(['noc', 'medal']).size().unstack(fill_value=0)
    tally['total'] = tally.sum(axis=1)
    tally.to_csv("final_medal_tally.csv")
    print("✅ Saved final_medal_tally.csv")


def main():
    print("🏁 Running Milestone 2 program...\n")

    start = time.time()

    # Step 1: Create initial CSVs (Milestone 1)
    writeOutputFiles()

    # Step 2: Load data
    data = load_data()
    print("Data loading complete.")

    # Step 3: Clean data
    for key, df in data.items():
        if not df.empty:
            data[key] = clean_data(df, df.columns[:2])
    print("Data cleaning complete.")

    # Step 4: Merge data
    merged = merge_datasets(data)

    # Step 5: Medal tally
    generate_medal_tally(merged)

    total = time.time() - start
    print(f"\n✅ Total runtime: {total:.2f}s")
    print("🎯 Milestone 2 completed successfully!")

if __name__ == "__main__":
    main()

