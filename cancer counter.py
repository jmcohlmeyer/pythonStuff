import csv
with open("/Users/jamie/Desktop/UNC Work Files/10012015-0114.csv", "r") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    prostate = 0
    kidney = 0
    bladder = 0
    for cancer in data:
    	if cancer[3] == "Bladder cancer":
    		bladder = bladder + 1
    	if cancer[3] == "Prostate cancer":
    		prostate = prostate + 1
    	if cancer[3] == "Kidney Cancer":
    		kidney == kidney + 1
    print("Prostate count = ")
    print(prostate)
    print ("Kidney count = ")
    print(kidney)
    print ("Bladder count = ")
    print(bladder)
