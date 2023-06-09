##Partial functions allow us to fix a certain number of arguments of a function and generate a new function.

from functools import partial


# A normal function
def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x


# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4)

# Calling g()
print(g(5))

### precision in python .. how to pring 2 of 3 numbers after the flotting point


a = 4.5671
import math
print(math.trunc(a))
print(math.ceil(a))
print(math.floor(a))
print('%.2f' % a)
print("{0:.3f}".format(a))
#####



