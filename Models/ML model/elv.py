import csv

input_file = "DATA/sqli.csv"
output_file = "sqli_cleaned.csv"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8", newline="") as outfile:
    lines = infile.readlines()
    cleaned_lines = [line.rstrip(',\n') + "\n" for line in lines]
    
    outfile.writelines(cleaned_lines)

print("Fichier nettoyé et sauvegardé sous", output_file)
