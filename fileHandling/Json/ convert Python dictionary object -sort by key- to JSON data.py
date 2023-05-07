import json
data = {
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }
print(type(data))
# convert to json data

json_obj = json.dumps(data,sort_keys=True,indent=4)
print(type(json_obj))
print(json_obj)

#print(json_obj["Name"])
#print(json_obj["Hobbies"])


###### 2

import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original String:")
print(j_str)
print("\nJSON data:")
print(json.dumps(j_str, sort_keys=True, indent=4))


######
