####### merge two dict
"""
d1 = {'name':'manish','age':'4'}
d2 = {'org':'pavilion','salary':'00'}

## way-1
d1.update(d2)
print(d1)

## way-2

for k in d2.keys():
    if k not in d1.keys():
        d1[k] = d2[k]
print(d1)



##### print fibonacci series

def fib(n):
    if n ==0 or n ==1:
        return 1
    return fib(n-1) + fib(n-2)
a = fib(10)
print(a)

##### print fact()

def fact(n):
    if n < 1:
        return 1
    return n*fact(n-1)

b = fact(5)
print(b)



##### 7 -Write a program to find sum of digits of an integer

a = 12234
sum = 0
for i in str(a):
    sum = sum + int(i)
print(sum)




####8.	Write a program to reverse digits of an integer

a = 12234
print(str(a)[::-1])




##### 9 Write a Python code using list comprehension to capitalize each word in a given string
#Input: A quick brown fox jumps over the lazy dog.
#Output: A Quick Brown Fox Jumps Over The Lazy Dog.

A= "A quick brown fox jumps over the lazy dog"
#print(A.title())

#OR
B = A.split()
new_str = [x.title() for x in A.split()]
s = " ".join(new_str)
print(s)




######13.Write a Python code using list comprehension to remove ‘the’ word from a given string
##Input: The quick brown fox jumps over the lazy dog.
##Output: quick brown fox jumps over lazy dog.


A= "The quick brown fox jumps over the lazy dog"
B = A.split()
for i in B:
    if i =='The' or i=='the':
        B.remove(i)
#C = [B.remove(x) if x=='The' or x=='the' else x for x in B ]
D = " ".join(B)
print(D)



######14. Write a Python code using list comprehension to return last five elements in given list in reverse order
#Input: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#Output: [100, 90, 80, 70, 60]

input = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#print(input[:-6:-1])
#OR
s = len(input)
n = 1
out = []
while n<=5:
    out.append(input[s-n])
    n+=1
print(out)





####15.	Write a Python method which will take input as string and return True
#### if given string has at least one capital letter, at least one small letter and one digit in it

import re
s = "RAM123amd"
def input_str(s):
    
    print(p)
    # if p:
    #     return True
a = input_str(s)
print(a)

"""

a = [10,120,10,20,20,212]
b = a.count(10)
print(b)
z



