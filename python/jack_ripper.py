import csv
with open('jack_ripper.csv', 'r') as csvfile:
    jack = csv.reader(csvfile)
    first_part = [row for row in jack]

print(first_part[0])

with open('jack_ripper.csv', 'r') as csvfile:
    jack = csv.reader(csvfile)
    all_texts = [row for row in jack]

press_reports = [row[4] for row in jack]
print(press_reports[0])
