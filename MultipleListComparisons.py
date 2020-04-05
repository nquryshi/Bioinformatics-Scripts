import csv
import pandas as pd 

# Get all the unique values amongst the different lists
# Find similarities between the two lists

with open('/Users/nabeelquryshi/Downloads/Mike.csv') as csvfile:
    reader = csv.reader(csvfile)
    colnames = next(reader)

colnames[0] = 'A'
print(colnames)

data = pd.read_csv('/Users/nabeelquryshi/Downloads/Mike.csv', names=colnames)

Genes = data.B.tolist()
F = data.F.tolist()
K = data.K.tolist()
H = data.H.tolist()
M = data.M.tolist()

MergedList1 = list(set(F+K+H+M))

FinalList = list(set(Genes).intersection(MergedList1))

print(len(FinalList))

with open("/Users/nabeelquryshi/Downloads/MikeAnalysis.txt", "w") as f:
    for item in FinalList:
        f.write("%s\n" % item)