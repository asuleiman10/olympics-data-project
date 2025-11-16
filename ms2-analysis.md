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
