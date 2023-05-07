"""
#######11. Pickling and unpickling

Defination :-
		Pickling in python is primarily used to serializing and desirializing a python object stucture.
		In other words it is a process of converting python objects into a byte stream to store it in a file or database.

Benifits :-
		1. Maintain programm states across sessions
		2. Or transport data over the network
		3. You can convert any object like file object/ dictionary object into the byte stream and convert back into it original form.

"""
## Example-1 with dict_obj

import pickle

data_dict = {"name":"manish","age":40,"address":"pune"}

#serialize this dict object into a file
filename = "data.pkl"
pickle.dump(data_dict,open(filename,"wb"))   #<< it will generate the file and saved dict_data into binary form.

#Desirialize the data
out  = pickle.load(open(filename,'rb'))
print(out)
