'''
Created on Jan 2, 2019

@author: nwijesinha

This exercise is to create a binary search implementation using python

'''
from numpy.distutils.fcompiler import none


# define a function for binary search
def bSearch(list, val):
    # assign the list size to a variable name list_size
    list_size = len(list) - 1
    # Set 0 as index 0 and list size to index n 
    idx0 = 0
    idxn = list_size
    # find the middle most value
    while idx0 <= idxn:
        midval = (idx0 + idxn) // 2
        
        if list[midval] == val:
            return midval
        # Compare the value with middle most value
        if val > list[midval]:
            idx0 = midval + 1
        else:
            idxn = midval - 1
    
    if idx0 > idxn:
        return None
    
    
# initialize a list
list = [72, 34, 19, 53, 7, 2]

# print the list values
print("Printing the list")
for i in list:
    print(i)
print('*' * 20)

# sort the list
list.sort()

# print the list values
print("Printing the sorted list")
for i in list:
    print(i)
print('*' * 20)

# Search the list for 72 and 11
print(bSearch(list, 72))
print(bSearch(list, 11))
print(bSearch(list, 19))
