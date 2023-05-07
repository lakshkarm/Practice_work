### reff https://www.geeksforgeeks.org/python-programming-language/
## creating sets
set_1 = set()
print(set_1)

# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

## pass list in a set
L = [1,2,3,4,5,6,12,12,1,2,2,3,4,5]
set_2 = set(L)
print(set_2)

##Creating a set with another method
my_set = {1, 2, 3,1,2,3,4,5,66}
print(my_set)

###add()
my_set.add(77)
print(my_set)

###update
my_set.update(["rishi","kumar",21,21,34])
print(my_set)

for i in my_set:
    print(i, end=" ")






