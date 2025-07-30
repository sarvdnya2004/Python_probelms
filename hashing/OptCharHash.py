s = "asedasedfgased"
li = ['a','s','e','d','f','g']

dict1 = {}

result = {}
for i in s:
    dict1[i] = dict1.get(i,0)+1
print(dict1)


