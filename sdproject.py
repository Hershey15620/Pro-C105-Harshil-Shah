import math
import csv
from os import read

with open("sdprojectdata.csv", newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data= file_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+= int(x)
    mean= total/n
    return mean


squared_list=[]
for i in data:
    a=int(i)-mean(data)
    a= a**2
    squared_list.append(a)

sum=0
for j in squared_list:
    sum= sum+j

result= sum/(len(data)-1)

stddev= math.sqrt(result)
print(stddev)