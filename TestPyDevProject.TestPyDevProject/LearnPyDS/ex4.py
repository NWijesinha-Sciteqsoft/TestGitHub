'''
Created on Nov 20, 2018

@author: nwijesinha

This exercise to learn dictionary or dict in python
Dictionary (Dict):
In Dictionary each key is separated from its value by a colon (:), 
the items are separated by commas, and the whole thing is enclosed in curly braces. 
An empty dictionary without any items is written with just two curly braces, like this: {}.

'''
# Define disctionary
dict1 = {'Name':"Zara", 'Age':7, 'Class': "First"}

# Print all the keys in a dictionary
print("Printing dictionary: ", dict1)
print("_"*20)
# Print a key with in a dictionary
print("dict['Name']: ", dict1['Name'])
print("dict['Age']: ", dict1['Age'])

# Accessing a key which is not part of dictionary, this throws an error
# print("dict['Alice']: ", dict['Alice'])
print("_"*20)
# Update an existing entry in a dictionary
dict1['Age'] = 8
# Add a new entry into dictionary
dict1['School'] = "DPS School"
# Print all the keys in a dictionary
print("Printing dictionary: ", dict1)
print("_"*20)
# Looping through dictionary to extract elements
for i, value in dict1.items():
    print("dict[%s]: " % i, value)
print("_"*20)
    
# Delete an element from a dictionary
print("Printing dictionary before delete")
for i, value in dict1.items():
    print("dict[%s]: " % i, value)
print("_"*20)
# deleting School from dictionary
del dict1['School']
# Looping through dictionary to extract elements
print("Printing dictionary after delete")
for i, value in dict1.items():
    print("dict[%s]: " % i, value)
print("_"*20)

# Clear an element from a dictionary
print("Printing dictionary before clear")
print(dict1)
print("_"*20)
# Clear dict1
dict1.clear()
print("Printing dictionary after clear")
print(dict1)
print("_"*20)

# Delete entire dictionary
print("Printing dictionary before clear")
dict1 = {'Name':"Zara", 'Age':7, 'Class': "First"}
print(dict1)
print("_"*20)
# Clear dict1
del dict1
print("Printing dictionary after clear")
print(dict1)
print("_"*20)
