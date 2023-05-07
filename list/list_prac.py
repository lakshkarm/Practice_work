string  = "hello what is this  "
print(string.strip( " "))
print(string)


#### insert function in the list

L = list(string)
L.insert(5,"mat")
print(L)

#### add multiple element at the end of the list at once

List = [1, 2, 3, 4]
List.extend([8, 'Geeks', 'Always'])
print(List)

### reverse the list
List.reverse()
print(List)
print(List[:-1:])

### remove   . it remove the same valuse if present in the list
List.remove(2)
print(List)

### pop .. it remove from the index
print(List[::-1])