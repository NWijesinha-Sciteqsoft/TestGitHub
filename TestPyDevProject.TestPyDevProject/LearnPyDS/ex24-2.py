'''
Created on Jan 4, 2019

@author: nwijesinha

This exercise is to learn about creating sort algorithms in Python
Sorting refers to arranging data in a particular format
Sorting algorithm specifies the way to arrange data in a particular order
Common orders are in numerical and lexicographical order
Five implementations of sort algorithms are
- Bubble Sort
- Merge Sort
- Insertion Sort
- Shell Sort
- Selection Sort

This exercise is to create a merge sort algorithm
Merge sort first divides the array into equal halves and then combines them in a sorted manner

'''

      
# Function to merge the sorted halfs
def merge(left_half, right_half):
    lhalf = left_half
    rhalf = right_half
    res = []
    while len(lhalf) != 0 and len(rhalf) != 0:
        if lhalf[0] < rhalf[0]:
            res.append(lhalf[0])
            lhalf.remove(lhalf[0])
        else:
            res.append(rhalf[0])
            rhalf.remove(rhalf[0])
        
    if len(lhalf) == 0:
        res = res + rhalf
    else:
        res = res + lhalf 
    return res

    
# define a function for merger sort
def mergeSort(uns_list):
    if len(uns_list) <= 1:
        return uns_list
    # find middle poing and devide it
    middle = len(uns_list) // 2
    llist = uns_list[:middle]
    rlist = uns_list[middle:]
    
    llist = mergeSort(llist)
    rlist = mergeSort(rlist)
    return list(merge(llist, rlist))

             
uns_list = [64, 34, 25, 12, 22, 11, 98] 
print(mergeSort(uns_list))
