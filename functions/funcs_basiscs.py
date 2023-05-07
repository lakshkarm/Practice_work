list1 = ['g', 'e', 'e', 'k', 's']
print("-----".join(list1))


dic = {'Geek': 1, 'For': 2, 'Geeks': 3}

# Joining special character with dictionary
string = '_'.join(dic)

print(string)


#####


number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']


# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)

#####

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
print(simpleGeneratorFun())
for value in simpleGeneratorFun():
    print(value)


####

def fun():
    str = "geeksforgeeks"
    x = 20
    return(str, x)# Return tuple, we could also
                    # write (str, x)
    #return[str, x]  ## return list
    #return str, x   ## return values

# Driver code to test above method
str= fun() # Assign returned tuple
print(str)
#print(x)

###

from dataclasses import dataclass


@dataclass
class Book_list:
    name: str
    perunit_cost: float
    quantity_available: int = 0

    # function to calculate total cost
    def total_cost(self):# -> float:
        return self.perunit_cost * self.quantity_available


book = Book_list("Introduction to programming.", 300.00, 3)
x = book.total_cost()

# print the total cost
# of the book
print(x)

# print book details
print(book)
