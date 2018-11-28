'''
Created on Nov 27, 2018

@author: nwijesinha

This exercise is to learn Maps in python
Maps:
Python Maps also called ChainMap is a type of data structure to manage multiple dictionaries together as one unit.
The combine dictionaries contains the key and value pair in a specific sequence eliminating any duplicate keys.
ChainMaps behave as a stack data structure

'''

# Import libraries for the program
import collections

# Create two dictionaries to store days of the week  
dict1 = {'day1': 'Mon', 'day2': 'Tue'}  # dict 1 has Mon and Tue
dict2 = {'day3': 'Wed', 'day1': 'Thu'}  # dict 2 has Wed Thu

# Define res object using collections.ChainMap then allocate dict1 and dict2
res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print("Printing the ChainMap")
print(res.maps, '\n')  # print the dictionary
print('*' * 50)

# print the keys
print("Printing the ChainMap keys and values")
print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print('*' * 50)

# Printing all the elements from the result
print('Printing all the elements')
for key, value in res.items():
    print('{} = {}'.format(key, value))
print('*' * 50)

# find a specific value in a result
print('day3 in res: {}'.format('day1' in res))  # ChainMap does have keys and values for day1 this should be True
print('day4 in res: {}'.format('day4' in res))  # ChainMap does not have key and value for day4 this should be False
print('*' * 50)

# Reordering ChainMaps
# Define res2 object using collections.ChainMap then allocate dict2 and dict1 in this oder
res2 = collections.ChainMap(dict2, dict1)

# Print the res and res2
print("Printing res ChainMap")
print(res.maps, '\n')  # print the dictionary
print('*' * 50)
print("Printing res2 ChainMap")
print(res2.maps, '\n')  # print the dictionary
print('*' * 50)

# Updating an element in dictionary
# Create two dictionaries to store days of the week  
dict3 = {'day1': 'Mon', 'day2': 'Tue'}  # dict 1 has Mon and Tue
dict4 = {'day3': 'Wed', 'day4': 'Thu'}  # dict 2 has Wed and Thu

# Define res object using collections.ChainMap then allocate dict1 and dict2
res3 = collections.ChainMap(dict3, dict4)

# Creating a single dictionary
print("Printing the ChainMap before update")
print(res3.maps, '\n')  # print the dictionary
print('*' * 50)

# Update key day4 to Fri in dictionary 2
dict4['day4'] = 'Fri'

# Creating a single dictionary
print("Printing the ChainMap after Updating")
print(res3.maps, '\n')  # print the dictionary
print('*' * 50)

# Adding a element to the Chain Map using update function
# restore day 4 to Thu
dict4['day4'] = 'Thu'
# Creating a single dictionary
print("Printing the ChainMap before inserting")
print(res3.maps, '\n')  # print the dictionary
print('*' * 50)

# Add an element using update function with day5 = Fri
res3.update({'day5':'Fri'})

# Creating a single dictionary
print("Printing the ChainMap after inserting")
print(res3.maps, '\n')  # print the dictionary

print("printing dictionary 3\n", dict3)
print("printing dictionary 4\n", dict4)
print('*' * 50)
