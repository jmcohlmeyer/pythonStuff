import csv
with open("/Users/jamie/Desktop/UNC Work Files/10012015-0114.csv", "r") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    print(data)
