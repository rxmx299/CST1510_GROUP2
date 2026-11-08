"""
RECORD CHECK  -  my version
===========================

Name  : Rama Ehab
Lane  :  AI 
Date  : 07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
df = pd.read_csv("dataset_records.csv") # reads the dataset records from the CSV file into a DataFrame

# ================================================================= PROCESS
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100 # calculates the percentage of rows loaded

# used lambda to assigns a status to each dataset based on its percentage
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >=90 else "OK")
# ================================================================== OUTPUT
# displays all records, including their perentage and status
print("All datasets:")
print(df)

status_not_ok = df[df["status"] != "OK"] # filteing by status to get datasets that are not OK

print("\nDatasets with status other than OK:")
print(status_not_ok)

# grouping records by status and count the rows in each group
status_counts = df.groupby("status").size() 

print("\nNumber of datasets per status:")
print(status_counts)

df.to_csv("dataset_records_report.csv", index=False) # saves all records to a new CSV without including row index

import matplotlib.pyplot as plt
# creates a bar chart showing the number of datasets in each status
status_counts.plot(kind="bar")
# adds a chart title and labels for the x and y axes
plt.title("Dataset counts by status")
plt.xlabel("Status")
plt.ylabel("Number of datasets")
plt.tight_layout() # adjusts the spacing to help prevent labels from being cut off
plt.savefig("data_status_counts.png") # saves the bar chart as a PNG image file
plt.show() # displays the bar chart
# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
