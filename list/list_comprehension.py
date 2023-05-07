L = [1,2,3,4,5,6]
print([x for x in L])
print([x*2 for x in L])
print([x*2 for x in L if x%2==0])


print(L.index(4))
L.reverse()
print(L)
a = L.copy()
print(a)
b = sum(a)
print(b)

###

print(max(a))
print(min(a))

###
for i,k in enumerate(a):
    print(i,k)

###

