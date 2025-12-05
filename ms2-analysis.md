# Milestone 2 – Olympics Data Project  
**Name:** Angel Suleiman  
**Group:** 3  
**Date:** November 2025  

---

## 1. Assumptions and Decisions

For this milestone, my main task was to upgrade my Milestone 1 prototype so that it could read, clean, and merge real Olympic data, including the new Paris 2024 datasets.  
The original files created in Milestone 1 were empty placeholders, so I treated them as older Olympic records that would later be filled. The Paris datasets (`paris_athletes.csv`, `paris_events.csv`, `paris_medallists.csv`) were used to simulate new incoming data.  

To make the program run smoothly, I made the following decisions:
- Skip empty CSVs to avoid crashes during testing.  
- Use `try` and `except` to handle missing or unreadable files.  
- Store all loaded files inside a dictionary for easy access.  
- Combine datasets with `pandas.concat()` instead of manual loops.  
- Clean each dataset by removing missing and duplicate rows, and trimming strings.  
- Track total runtime using Python’s `time` module.

---

## 2. Data Structures Used

### Dictionary
I used a **dictionary** called `data` to hold all datasets:
```python
data = { "paris_athletes": DataFrame, "paris_events": DataFrame, ... }



Name: Ashish Dilipbhai Solanki
Group: 3
Date: November 2025

1. Assumptions and Decisions

For this milestone, my main task was to implement the medal tally section of the project and update the prototype so it no longer relied on pandas. Since the Milestone 1 files were mostly empty placeholders, I treated them as older Olympic records and used the Paris medal file (paris_medallists.csv) as the main dataset to verify that my logic worked correctly.

Because some files might be missing or contain no rows, I added conditions to skip empty CSVs to avoid errors. I also wrote helper functions to handle variations in column names (such as "NOC", "noc", or "Team_NOC"), since the datasets did not always follow the same format.

To keep the program consistent and within restrictions, I made the following decisions:

Use only Python’s built-in modules (csv, dictionaries, lists, sets).

Group medal results by (edition_id, NOC) using a dictionary.

Track unique athletes with a set so each athlete is counted only once.

Keep the output format identical to the required new_medal_tally.csv.

Convert the final results into a list of dictionaries for writing to the CSV file.

2. Data Structures Used
Dictionary

I used a dictionary called medal_tally where each key represents a combination of the Olympic edition and the NOC:

key = (edition_id, NOC)


Each entry stores:

edition

edition_id

Country

NOC

set of athlete IDs

gold, silver, and bronze medal counts

This allowed medal totals to be updated easily while processing each event row.

Set

A set was used to track unique athlete IDs:

info["athletes"].add(athlete_id)


This ensures that an athlete is not counted multiple times, even if they appear in more than one event.

List of Dictionaries

After completing the medal calculations, I converted the dictionary into a list of row dictionaries so it could be written to new_medal_tally.csv in the correct header order.

Summary

My contribution for Milestone 2 was implementing the medal tally system using only core Python features. This included loading the necessary files, organizing medal results, counting athletes and medals, and generating the final output file. My work replaces the earlier pandas-based version and ensures the project follows all required restrictions.
