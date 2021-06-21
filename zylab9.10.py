"Peter Nguyen"
"6/20/2021"
"CIS2348"
"1860823"
"9.10 CIS 2348 LAB: Word frequencies (lists)"


import csv


fileName = input()
wordsFrequency = {}

with open(fileName, 'r') as csvfile:
    csv = csv.reader(csvfile)
    for row in csv:
        for word in row:
            if word not in wordsFrequency.keys():
                wordsFrequency[word] = 1
            else:
                wordsFrequency[word] += 1

for key in wordsFrequency.keys():
    print(key + " " + str(wordsFrequency[key]))