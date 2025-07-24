li = [11,12,23,34,45,23,34,45,45,12]

dict = {}

for i in li:
    dict[i] = dict.get(i,0)+1

print(dict)