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

def main():
    print("✅ Milestone 1 prototype running…")
    writeOutputFiles()
    print("✅ All 5 CSV files created!")

if __name__ == "__main__":
    main()

