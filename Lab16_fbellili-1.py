"""
Program: Lab 16 - Plot Ohio Unemployment Data
Author: Farouk Bellili
Purpose: Parse the data using the csv module, convert date strings
         to datetime objects, and produce PNG image file.
Starter Code: none
Date: 05-11-26
"""
 
import matplotlib.pyplot as plt
import csv
from datetime import datetime
 
dates = []
rates = []
 
with open("OHUR.csv", newline="") as csv_file:
    reader = csv.reader(csv_file)
 
    # Use enumerate() to identify and skip the header row.
    for index, row in enumerate(reader):
        if index == 0:
            print(f"Header: {row}")
            continue
 
        try:
            # Convert date string to a datetime object for proper axis scaling.
            date = datetime.strptime(row[0], "%Y-%m-%d")
            rate = float(row[1])
            dates.append(date)
            rates.append(rate)
        except ValueError as e:
            print(f"Skipping row {index} due to error: {e}")
 
plt.plot(dates, rates)
plt.title("Ohio Unemployment Rate (by Month): 1976 - 2022")
plt.xlabel("Date")
plt.ylabel("Unemp Rate")
 
plt.gcf().autofmt_xdate()   # Rotate date labels so they don't overlap.
 
plt.savefig("ohio_unemployment.png")
plt.show()
