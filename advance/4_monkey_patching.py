"""
Defination :-
		Monkey patching is the technich where you change the class attribute behavior dynamically.
		Or
		The term monkey patch refers to dynamic (or run-time) modifications of a class or module.
		In Python, we can actually change the behavior of code at run-time.






class student:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        print(self.name)


obj1 = student("Manish")
obj1.get_name()

# write another function
def change_name(new_name):
   return new_name

# lets do monkey patching here
obj1.get_name=change_name("rishi")
print(obj1.get_name)

"""

import requests
# def get_data()->dict:
#     request  = requests.get('https://jsonplaceholder.typicode.com/todos/1')
#     data:dict = request.json()
#     return data

def get_data():
    request = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    data = request.json()
    return data

print("before=",get_data())

def get_updated_data():
    return {"user":"manish","id":12345}

##Now lets assign update the value -using monkey patching
get_data = get_updated_data
print("After=",get_data())



#### Example-3

def get_data_1():
    return {"Hello" : "World"}

requests.get = get_data_1
print(requests.get())