def square_root():
    L = [1,2,3,4,5]
    for i in L:
        yield i*2

a = square_root()
for i in range(6):
    print(next(a))


