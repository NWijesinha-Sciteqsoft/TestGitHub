'''
Created on Dec 31, 2018

@author: nwijesinha

This exercise to create a heap using python
Heap is created using python built in library heapq

'''

import heapq

# Define a variable to hold an array of num
H = [21, 1, 45, 78, 3, 5]

# pint the array
print('Print the array before using heapify')
print(H)

# use heapify to rearrange the elements
heapq.heapify(H)

# pint the array
print('Print the array after using heapify')
print(H)

# adding an element to heap
heapq.heappush(H, 8)

# pint the array
print('Print the array after adding an element')
print(H)

# removing an element from the heap
# pop will remove the element in index position 1
heapq.heappop(H)

# pint the array
print('Print the array after deleting an element')
print(H)

# heapreplace fucntion always removes the smallest element of the heap and inserts the new element at some place
heapq.heapreplace(H, 6)

# pint the array
print('Print the array after replacing an element')
print(H)

