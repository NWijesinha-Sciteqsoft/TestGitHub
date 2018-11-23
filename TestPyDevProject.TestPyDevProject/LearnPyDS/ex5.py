'''
Created on Nov 21, 2018

@author: nwijesinha

This exercise to learn 2D Arrays in python
Two dimensional array is an array within an array. It is an array of arrays. 
In this type of array the position of an data element is referred by two indices instead of one. 
So it represents a table with rows and columns of data. 
In the below example of a two dimensional array, observer that each array element itself is also an array.

'''
# Import libraries
from array import *

# Define a two dimentional array
temp1 = [[11, 12, 5, 2],
         [15, 6, 10],
         [10, 8, 12, 5],
         [12, 15, 8, 6]]

# Print 2D array
print(temp1)
print("_"*20)  # print _ 20 times
# Print 2D array by looping
for i in range(len(temp1)):
    for j in range(len(temp1[i])):
        print("Temp for day %i is: " % i, temp1[i][j])
print("_"*20)  # print _ 20 times
# Printing 2D array looping another way of looping 
for r in temp1:
    for c in r:
        # print the elements with space
        print(c, end=" ")
    print()  # move to next line
print("_"*20)  

# inserting elements into the 2D array
# inserting elements to index position 2
# Printing 2D array looping another way of looping 
print("Printing before inserting the elements")
for r in temp1:
    for c in r:
        # print the elements with space
        print(c, end=" ")
    print()  # move to next line
print("_"*20) 
# inserting using insert function of 2D array
temp1.insert(2, [0, 5, 11, 13, 6])
print("Printing after inserting the elements")
for r in temp1:
    for c in r:
        # print the elements with space
        print(c, end=" ")
    print()  # move to next line
print("_"*20) 

# Updating elements in 2D array
# Printing 2D array looping another way of looping 
print("Printing before updating the elements")
for r in temp1:
    for c in r:
        # print the elements with space
        print(c, end=" ")
    print()  # move to next line
print("_"*20) 
# updating elements in index 2
temp1[2] = [11, 9]
# Printing 2D array looping another way of looping 
print("Printing after updating the elements")
for r in temp1:
    for c in r:
        # print the elements with space
        print(c, end=" ")
    print()  # move to next line
print("_"*20)

# deleting element of a 2D array
# Printing 2D array looping another way of looping 
print("Printing before deleting the elements")
for r in temp1:
    for c in r:
        # print the elements with space
        print(c, end=" ")
    print()  # move to next line
print("_"*20) 
# Deleting elements in index 3
del temp1[3]
# Printing 2D array looping another way of looping 
print("Printing after deleting the elements")
for r in temp1:
    for c in r:
        # print the elements with space
        print(c, end=" ")
    print()  # move to next line
print("_"*20) 
