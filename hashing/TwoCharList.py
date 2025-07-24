s = "aabcdeeeffdddd"
li = ['a','b','c','d','e','f','g']

li2 = list(s)

dict = {}

for i in li2:
    dict[i] = dict.get(i,0)+1

result = {}

for i in li:
    result[i] = dict.get(i,0)

print(result)