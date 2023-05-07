def test_deco(func):
    print("this is decorator function")
    def wrapper_func(x,y):
        if y > x:
            x,y = y,x
        return func(x,y)
    return wrapper_func

@test_deco   ####<<<<<<<<<<<<<<<<<<<<<< use decorator while writing the function rather calling the func
def divition(x,y):
    return(x/y)

print(divition(5,10))

