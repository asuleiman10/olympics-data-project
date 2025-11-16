# Olympics Data Project – Milestone 1 & 2

**Course:** Data Structures and Algorithms  
**Group:** 3 

### 👥 Members
- **Ashish Dilipbhai Solanki** – Medal Tally Calculation  
- **Angel Suleiman** – Data Cleaning & Integration  
- **Josclif Taah** – Games & Country Data Modules  

---

## 🧩 Project Overview
This project focuses on organizing, cleaning, and analyzing Olympic datasets in preparation for statistical analysis.  

In **Milestone 1**, our goal was to build a simple prototype that created CSV output files with the correct structure.  
In **Milestone 2**, we upgraded the prototype into a fully functional data-processing program that merges, cleans, and analyzes real Olympic and Paris 2024 data.

---

## 🥇 Milestone 1 Summary
### Objectives:
- Set up the project repository and test version control.  
- Understand the dataset and identify missing or inconsistent entries.  
- Create a basic prototype that generates the required CSV output structure.  

### Outputs:
- Generated 5 empty CSV placeholders (`new_*.csv` files).  
- Verified all file headers matched project requirements.  

---

## 🏆 Milestone 2 Summary
### Objectives:
- Integrate and clean Paris 2024 datasets (`paris_athletes.csv`, `paris_events.csv`, `paris_medallists.csv`).  
- Merge Paris data with previous Olympic datasets.  
- Handle missing and duplicate entries using Pandas.  
- Generate a final medal tally file summarizing all results.  

### Features Implemented:
- Data cleaning (removal of missing/duplicate values, lowercase formatting).  
- CSV validation and handling of empty files using `try–except`.  
- Runtime tracking using Python’s `time` module.  
- Merging datasets with `pandas.concat()` for performance.  
- Medal tally generation grouped by NOC and medal type.  

### Program Output:
- ✅ `final_medal_tally.csv` successfully created  
- ✅ Total runtime: **≈ 0.03 seconds**

---

## 📂 Project Files
| File | Description |
|------|--------------|
| `project.py` | Main Python program (data cleaning, merging, medal tally) |
| `ms2-analysis.md` | Individual analysis (Angel Suleiman) |
| `prompts.md` | Resource & AI usage log for all members |
| `tasks.md` | Group task tracking and responsibilities |
| `new_*.csv` | Placeholder CSVs created during Milestone 1 |
| `paris_*.csv` | Paris 2024 dataset samples used for Milestone 2 |

---

## 🧠 Notes
- Each group member contributed through commits to the shared repository.  
- All analysis, code, and documentation were verified locally before committing.  
- The project was designed to maintain data consistency, handle large files, and meet runtime requirements (< 50 seconds per GitHub Actions policy).

---

📅 **Final Submission Date:** December 1, 2025  
💻 **Repository:** [asuleiman10 / olympics-data-project](https://github.com/asuleiman10/olympics-data-project)
