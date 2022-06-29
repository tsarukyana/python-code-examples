"""
You want to read or write data encoded as a CSV file.
"""
import csv

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
headers = next(f_csv)

for row in f_csv:
    # Process row
    pass
