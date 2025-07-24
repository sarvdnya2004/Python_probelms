n = [12,23,34,45,56]
m = [12,23,34,45,56,56,12,23,34,12,34,46,56,56]

freq_n = {}

for i in m:
    freq_n[i] = freq_n.get(i,0)+1

result = {}
for j in n:
    result[j] = freq_n.get(j,0)




print(sorted(result.items(), key = ))