import json

### https://www.w3resource.com/python-exercises/python-json-exercise-6.php

with open('file_1.json','r') as fh:
    p_obj = json.load(fh)
    print(p_obj)

with open('file_2.json','w') as fh:
    json.dump(p_obj,fh,indent=4)

with open('file_2.json','r') as fh:
    python_obj = json.load(fh)
    print(python_obj)
