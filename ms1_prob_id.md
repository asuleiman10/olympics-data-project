# Problem Identification – Milestone 1  

### Unknown or Wrong Data
While checking the data files, I noticed a few issues:  
- Some athlete birth dates are missing or written in different formats.  
- A few event results use different measurement units (like meters and feet).  
- Some countries have old or duplicate NOC codes.  

### How I Plan to Handle Wrong or Missing Data
- If data is completely missing, I’ll replace it with `NULL` so it’s easy to spot later.  
- For numbers like heights, times, or distances, I’ll make sure they’re all in the same unit (metric).  
- I’ll clean up country codes and use the latest NOC list for consistency.  

### How the Paris Data Is Organized
The Paris data is divided into separate CSV files — athlete bios, event results, countries, and games.  
Each file will be cleaned separately, then I’ll connect them using a common key (like athlete_id or country code).  
If there are duplicate athletes, I’ll check using their full name and birth date to keep only one record.  

### How I’ll Know My App Is Working
I’ll test by running the program and checking that all 5 new CSV files are created properly.  
I’ll also check that:  
- Each file has the right headers.  
- There are no crashes or empty outputs.  
- Some known athlete data shows up correctly in the cleaned files.  

---

**Summary:**  
This milestone was mainly to understand the data and plan how to clean and organize it.  
So far, the prototype runs and creates all the files as expected, which means the base setup is working.
