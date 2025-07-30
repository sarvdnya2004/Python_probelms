s = "asedasedfgased"
li = ['a','s','e','d','f','g']

dict = {}

for i in li:
    for j in s:
        if i == j:
            dict[j] = dict.get(i,0)+1

print(dict)
