"""
json.load() takes a file object and returns the json object.
It is used to read JSON encoded data from a file and convert it into a Python dictionary
and deserialize a file itself i.e. it accepts a file object.

import json

data = {
    "name": "Satyam kumar",
    "place": "patna",
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "xyz@gmail.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
with open( "data_file.json" , "w" ) as write:
    json.dump( data , write )



#2 json.loads()

json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
It is mainly used for deserializing native string, byte, or byte array which consists of
JSON data into Python Dictionary.


import json 
    
# JSON string: 
# Multi-line string 
data = "{
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }"

# parse data: 
res = json.loads( data ) 
    
# the result is a Python dictionary: 
print( res )


######################### json.dump() / Vs / json.dumps()
json.dumps()
json.dumps() method can convert a Python object into a JSON string.

Parameters:

dictionary – name of dictionary which should be converted to JSON object.
indent – defines the number of units for indentation

Ex--

import json
    
# Data to be written
dictionary ={
  "id": "04",
  "name": "sunil",
  "department": "HR"
}
    
# Serializing json 
json_object = json.dumps(dictionary, indent = 4)
print(json_object)



==json.dump()

json.dump() method can be used for writing to JSON file.

Syntax: json.dump(dict, file_pointer) 

Parameters:

dictionary – name of dictionary which should be converted to JSON object.
file pointer – pointer of the file opened in write or append mode.


import json
  
# Data to be written
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
  
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
    
"""
import json
data = {"Adm_no":'230',"Name":'sidhant',"Class":'sr.kg',"section":'a',"Marks":'32'}


with open('file_1.json','w') as fh:
    json.dump(data,fh)

# Reading from file
with open('file_1.json','r') as fh:
    a = json.load(fh)
    print(a)


### json.loads(string)

data = """{ 
    "Name": "Jennifer Smith", 
    "Contact Number": 7867567898, 
    "Email": "jen123@gmail.com", 
    "Hobbies":["Reading", "Sketching", "Horse Riding"] 
    }"""

# parse data:
res = json.loads(data)
print(res)

#####

