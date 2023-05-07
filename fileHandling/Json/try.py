import json
data = '{"employee":{"name":"John", "age":30, "city":"New York"}}'

print(type(data))  ## it is a json string
data_1 = json.loads(data)
print(type(data_1))  ## it is a json sting

# write this json sting into a file
with open('file_4_practice.json','w') as fh:
    json.dump(data_1,fh)

with open('file_4_practice.json','r') as fh:
    p_obj = json.load(fh)
    print(type(p_obj))
    print(p_obj)
    print(p_obj['employee'])



