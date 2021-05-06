# python3 -i demo5_csv.py
import csv

infilename = "demo_data_file.csv"
with open(infilename,"r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0].startswith("#"):
            continue
        time, binomial, gaussian = float(row[0]), int(row[1]), float(row[2])
# Reference: https://docs.python.org/3/library/csv.html
#            https://docs.python.org/3/library/string.html