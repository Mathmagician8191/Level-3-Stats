import csv

file = open("data.csv") #specify path of data here

raw_data = csv.reader(file, delimiter=",") #replace , with delimeter (if different, single character only)

data = []
for item in raw_data: data.append((item[0],item[1])) #replace 0 with value to compare and 1 with value to evaluate (stuff is 0-indexed)

dataset1 = []
dataset2 = []
for item in data[1:]: #remove [1:] if there is no header row
    if item[1] == "": #add name of item for dataset1 (must match exactly)
        dataset1.append(int(item[0])) #replace int() with float() if the data has more than just integers
    else: dataset2.append(int(item[0]))

iterations = 1000 #number of resamples
