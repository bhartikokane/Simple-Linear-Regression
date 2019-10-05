import csv
import math
filename = "data.csv"
rows = []
fields = []
xi = []
yi = []
sumx = 0
sumy = 0
sumbi = 0
sumx2 = 0
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile) 
    for row in csvreader: 
        rows.append(row)
for i in range(rows):
    sumx = sumx + int(rows[i][0])
    xm = sumx / len(rows)
    sumy = sumy + int(rows[i][1])
    ym = sumy / len(rows)
for j in range(len(rows)):
    xi.append(int(rows[j][0])-xm)
    yi.append(int(rows[j][1])-ym)
for k in range(len(rows)):
    sumbi = sumbi + xi[k]*yi[k]
    sumx2 =  sumx2 + math.pow(xi[k],2)
b1 = sumbi / sumx2
b0 = ym - b1 * xm
print(b1)
print(b0)
x = int(input("Enter a X value \n"))
y = b0 + b1 * x
print("Predicted Y value is %f"%(y))
