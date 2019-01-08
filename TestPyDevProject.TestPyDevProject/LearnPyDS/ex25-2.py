'''
Created on Jan 7, 2019

@author: nwijesinha

This exercise is to learn about searching a data structure in Python
Interpolation Search
This search algorithm works on the probing position of the required value. 
For this algorithm to work properly, the data collection should be in a sorted form and equally distributed. 
Initially, the probe position is the position of the middle most item of the collection.
If a match occurs, then the index of the item is returned. 
If the middle item is greater than the item, then the probe position is again calculated in the sub-array to the right of the middle item.
Otherwise, the item is searched in the sub-array to the left of the middle item. 
This process continues on the sub-array as well until the size of sub-array reduces to zero.

'''


def intpol_search(input_list, x):
    idx0 = 0
    idxn = (len(input_list) - 1)
    
    while idx0 <= idxn and x >= input_list[idx0] and x <= input_list[idxn]:
        # Find the mid point
        mid = idx0 + \
               int(((float(idxn - idx0) / (input_list[idxn] - input_list[idx0]))
                    * (x - input_list[idx0])))
        # Compare the value at mid point with search value
        if input_list[mid] == x:
            return "Found " + str(x) + " at index " + str(mid)
        
        if input_list[mid] < x:
            idx0 = mid + 1
    return "search element not in the list"

    
l = [2, 6, 11, 19, 27, 31, 45, 121]
print(intpol_search(l, 2))
print(intpol_search(l, 27))
print(intpol_search(l, 121))    
print(intpol_search(l, 151))       
