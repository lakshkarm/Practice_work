import json
# a Python object (dict):
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6
}
print(type(python_obj))
# convert into JSON:
j_data = json.dumps(python_obj,indent=4)

# result is a JSON string:
print(j_data)