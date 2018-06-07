import csv
with open('jack_ripper.csv', 'r') as csvfile:
    first_col = csv.reader(csvfile)
    first_part = [row for row in first_col]

print(first_part[0])

with open('jack_ripper.csv', 'w') as (meat):
    csvwriter = csv.writer(meat)
    
