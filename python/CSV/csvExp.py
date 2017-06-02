import csv

with open('file path', 'r') as f:
    f_csv = csv.reader(f, delimiter='\t')
    headers = next(f_csv)
    for i in f_csv:
        print int(i[2])

with open("file path", 'w') as f:
    f_csv = csv.writer(f, delimiter="\t")
    f_csv.writerow(["item"] * 5)
    f_csv.writerow(["item1", "item2", "item3"])

with open('stocks.csv', 'r') as f:
    ## the first line is header
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print row['xxx']

with open('file path', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    for i in data:
        f_csv.wirterow
