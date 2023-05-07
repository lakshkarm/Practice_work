###1 without recursion

def fib(n):
    out = 1
    for i in range(1,n+1):
        out = out*i
    return out
#print(fib(5))

####2 using recursion

def fib_r(n):
    if n == 1:
        return n
    return n*fib(n-1)
print(fib_r(11))