'''
Created on Nov 20, 2018

@author: nwijesinha
'''
# Import Libraries
from array import array

# Array of integers with 5 integers
array1 = array('i', [10,20,30,40,50])

# Print all Array elements
print("Priting array elements")
for i in array1:
    print(i)
    
# Access Array elements by index 
# Print element at index 0 or first element
print("Printing element One")
print(array1[0])
# Print element at index 2 or third element
print("Printing element Three")
print(array1[2])

# Adding an element in the middle of the array using insert()
print("adding 60 to element 1")
array1.insert(1, 60)

# Print all Array elements
print("Printing array elements")
for i in array1:
    print(i)
    
# Deleting an element using remove()
print("removing 40 from element 5")
array1.remove(40)

# Print all Array elements
print("Printing array elements")
for i in array1:
    print(i)
