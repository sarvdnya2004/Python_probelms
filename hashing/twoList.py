n = [12,23,34,45,56]
m = [12,23,34,45,56,56,12,23,34,12,34,46,56,56]

dict = {}

for i in n:
    count = 0;
    for j in m:
        if i == j:
            count +=1
    dict[i] = count

print(dict)