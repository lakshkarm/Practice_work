import json

data = '''{
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }'''

print(type(data))
# convert json data/string into python obj

python_obj = json.loads(data)
print(type(python_obj))
print(python_obj)
print(python_obj["Name"])
print(python_obj["Email"])