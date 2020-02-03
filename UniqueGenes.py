# This file takes as input a txt file with pre processed RNA-seq / CHIP-seq data and returns 
# the list of unique genes and their corresponding frequencies. 

from collections import Counter
import csv

# Get all of the gene names into one giant list

massiveList = []

with open('/Users/nabeelquryshi/Downloads/H3K27ac_HMG016_WITH_EXP_CRC_SCORES.txt') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        row = str(row)
        tmpStr = row.find(']')
        row = row[0:tmpStr+1]
        row = row[3:len(row)-1]
        rowList = list(row.split(', '))
        #print(rowList)
        for gene in rowList:
            gene = gene.replace("'","")
            massiveList.append(gene)
            #print("DONE")

# print(massiveList)

print(Counter(massiveList).keys())
print(Counter(massiveList).values())