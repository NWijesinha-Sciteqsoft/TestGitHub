'''
Created on Dec 12, 2018

@author: nwijesinha

This exercise is to create hash table in Python using dictionary data type.
The Keys in the dictionary satify the following requireemnts
 - The keys of the dictionary is hashable ie. they are generates by hashing fucntion which generated unique result for each unique value supplied by has function
 - The order of data elements in a dictionary is not fixed

'''

# Declare a dictionary
dict = {'Name' : 'Zara', 'Age' : 7, 'Class': 'First'}

# print hash table
print("Printing the has table")
print(dict)

# Accessing the dictionary with its key
print("dict[Name]: ", dict['Name'])
print("dict[Age]: ", dict['Age'])

dict['Age'] = 8  # updating the dictionary
dict['School'] = 'DPS School'  # adding a new entry to the hash table

# print hash table
print("Printing the has table")
print(dict)

# Accessing the dictionary with its key
print("dict[Age]: ", dict['Age'])
print("dict[Schoo]: ", dict['School'])

# Deleting  entries from hash table or dictionary
del dict['Name']  # deleting entry using key 'Name
# print hash table
print(dict)
# remove all entrise from dictionary or hash table
dict.clear()
print(dict)
# deleting has table or dictionary
del dict
print(dict)
print("dict[Age]: ", dict['Age'])
 
