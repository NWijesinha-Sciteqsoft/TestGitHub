'''
Created on Jan 2, 2019

@author: nwijesinha

This exercise is to create a recursive function in python
Recursion allows a function to call itself
Implement the binary algorithm using recursion

'''


# Define binary search with recursion
def bSearch(list, idx0, idxn, val):
    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
        # compare the search item with middle most value
        if list[midval] > val:
            return bSearch(list, idx0, midval - 1, val)
        elif list[midval] < val:
            return bSearch(list, midval + 1, idxn, val)
        else:
            return midval

        
# initiate a sorted list
list = [8, 11, 24, 56, 88, 131]

# search for 24 and 51
print(bSearch(list, 0, 5, 24))
print(bSearch(list, 0, 5, 51))
