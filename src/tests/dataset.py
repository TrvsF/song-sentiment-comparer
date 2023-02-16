import csv

reader = csv.DictReader(open('data/id_lang.csv'), delimiter='\t', quoting=csv.QUOTE_NONE)

for item in reader:
    print(item)