'''
Created on Nov 20, 2018

@author: nwijesinha

This exercise to introduce Array and using arrays in Python
Array: 
It is a sequential arrangement of data elements paired with the index of the data element
Array data elements can be only one data type, you cannot mix data types
Array data type has to be specified when initiated

'''
# Import Libraries
from array import array

# Array of integers with 5 integers
array1 = array('i', [10,20,30,40,50])

# Print all Array elements
print("Printing array elements")
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
print("adding element 60 to index 1")
array1.insert(1, 60)

# Print all Array elements
print("Printing array elements")
for i in array1:
    print(i)
    
# Deleting an element using remove()
print("removing element 40 from index 5")
array1.remove(40)

# Print all Array elements
print("Printing array elements")
for i in array1:
    print(i)
    
# Searching the array for element 40 index 4
array1.remove(60)
array1.insert(3, 40)
print("Printing array elements")
for i in array1:
    print(i)
print("Searching for index for element 40:")
print(array1.index(40)) 

# Updating or replacing element 
# Replace index 2 element with 80
print("Replace element 30 in index 2 with 80")
array1[2] = 80
print("Printing array elements")
for i in array1:
    print(i)
