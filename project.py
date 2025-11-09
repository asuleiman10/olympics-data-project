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

# ----------------- MILESTONE 2 STARTS HERE -----------------

import pandas as pd
import time

def load_data():
    """Load Olympic and Paris datasets"""
    files = [
        "new_olympic_athlete_bio.csv",
        "new_olympic_athlete_event_results.csv",
        "new_olympics_country.csv",
        "new_olympics_games.csv",
        "new_medal_tally.csv",
        "paris_athletes.csv",
        "paris_events.csv",
        "paris_medallists.csv"
    ]

    data = {}
 HEAD
    for f in files:
        try:
            df = pd.read_csv(f)

            # Skip empty CSVs
            if df.empty:
                print(f"⚠️ {f} is empty — skipped.")
                continue

            data[f.split('.')[0]] = df
            print(f"Loaded {f}")

        except FileNotFoundError:
            print(f"⚠️ Missing file: {f}")
        except pd.errors.EmptyDataError:
            print(f"⚠️ {f} has no data — skipped.")
    return data

for f in files:
    try:
        # Try reading the file
        df = pd.read_csv(f)

        # Skip completely empty CSVs
        if df.empty:
            print(f"⚠️ {f} is empty — skipped.")
            continue

        # Store loaded DataFrame
        data[f.split('.')[0]] = df
        print(f"Loaded {f}")

    except FileNotFoundError:
        print(f"⚠️ Missing file: {f}")
    except pd.errors.EmptyDataError:
        print(f"⚠️ {f} has no data — skipped.")
return data

 d36c36e4fd1d2ee6c8e1af8a71e5b8d0daa7a6c3



def clean_data(df, cols):
    """Remove missing and duplicate records"""
    df.dropna(subset=cols, inplace=True)
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].astype(str).str.strip().str.lower()
    df.drop_duplicates(inplace=True)
    return df


def merge_datasets(data):
    """Merge old and Paris event results"""
    old_results = data.get("new_olympic_athlete_event_results", pd.DataFrame())
    paris_results = data.get("paris_medallists", pd.DataFrame())

    combined = pd.concat([old_results, paris_results], ignore_index=True)
    print(f"✅ Combined results shape: {combined.shape}")
    return combined


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

