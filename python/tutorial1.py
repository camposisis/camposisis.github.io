import csv
with open('basic.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    names = [row for row in our_reader]
print(names)
print(names[1])

print(len(names))
#find the length of each first names
for row in names:
    print(len(row[2]))
#find the longest first names
longest = ""
for row in names:
    if len(row[2]) > len(longest):
        longest = row [2]
print(longest)

#construct a new list consisting of only the first names we have hereself.
first_names = [row[2] for row in names]
first_names.reverse()
print(first_names)

new_row = [2, 'wayne', 'graham', 'meh']
names.append(new_row)
print(names)

a_row = [3,'fox','eliza','SO COOL']
print(names + a_row)

with open('practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for i in range(0, 100, 10):
        csvwriter.writerow([i, i + 5, i + 15, i + 20])

with open('practice.csv', 'r') as fin:
    our_reader = csv.reader(fin)
    data = [row for row in our_reader]
print(data)

data [3][1] = 'Ethan'
data [4][1] = 'Brandon'
data [2][1] = 'Tony the cat'

with open ('practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for row in data:
        csvwriter.writerow(row)

print(data)

groceries = []
with open('shopping.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        groceries.append(row)

print(groceries)

print(groceries[2]['name'])

for item in groceries:
    print(item['name'])

tony = {'name':'tony', 'nutritious': 'False', 'id': '5' }

groceries.append(tony)

with open ('updated_groceries.csv', 'w') as fout:
    column_names = ['id', 'name', 'nutritious']
    dictwriter = csv. DictWriter(fout, fieldnames=column_names)
    dictwriter.writeheader()
    for row in groceries:
        dictwriter.writerow(row)
