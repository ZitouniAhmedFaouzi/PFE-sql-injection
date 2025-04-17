
import csv
import chardet
import pandas as pd

input_file = "DATA/sqli.csv"
output_file = "SQLIV3_cleanedddddddd.csv"

# Detect file encoding
with open(input_file, "rb") as f:
    result = chardet.detect(f.read())

# Read and clean the file
with open(input_file, "r", encoding=result['encoding']) as infile, open(output_file, "w", encoding=result['encoding'], newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        if len(row) == 2:  # Keep only lines with exactly 2 fields
            writer.writerow(row)