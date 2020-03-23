
# This file takes as input a txt file with pre processed RNA-seq / CHIP-seq data and returns 
# the list of unique genes and their corresponding frequencies. 

from collections import Counter
import csv
import tkinter as tk
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.withdraw() # Stop root directory from appearing
filename = askopenfilename() # Get the path from the person
#print(filename) 

LastInstanceSlash = filename.rfind("/")
OutputDirectory = filename[0:LastInstanceSlash + 1] + "output.txt"

# Get all of the gene names into one giant list

massiveList = []

with open(filename) as f:
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

#print(Counter(massiveList).keys())
#print(Counter(massiveList).values())

# Create a popup (GUI) that opens file chooser and outputs the file

f = open(OutputDirectory, "w+")
tmpDict = Counter(massiveList)
for key in tmpDict:
    #print(tmpDict[key])
    tmpStr = key + "\t" + str(tmpDict[key]) + "\n"
    f.write(tmpStr)