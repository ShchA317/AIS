import csv
import collections

with open("data/matrix-without-headers.csv") as file_name:
    file_read = csv.reader(file_name)
    array = list(file_read)

f = open("data/city-list.txt","r")
lines = f.readlines()

array1 = []

for line in lines:
    data = line.split()
    dict1={data[1]:data[0]}
    array1.append(dict1)

res1 = collections.ChainMap(array1)
print(res1)
