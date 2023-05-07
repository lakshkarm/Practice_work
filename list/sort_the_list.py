l1 = [6, 4, 11,15, 24, 19, 25, 27, 30,17, 1]

for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i] < l1[j]:
            continue
        else:
            l1[i], l1[j] = l1[j], l1[i]
print(l1)
