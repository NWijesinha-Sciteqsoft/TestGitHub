'''
Created on Jan 7, 2019

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

Insertion sort involves finding the right place for a given element in a sorted list

'''


# Insertion sort function
def insertionSort(inputList):
    
    for i in range(1, len(inputList)):
        j = i - 1
        nxt_element = inputList[i]
    
        # Compare the current element with next one
        while (inputList[j] > nxt_element) and (j >= 0):
            inputList[j + 1] = inputList[j]
            j = j - 1
        inputList[j + 1] = nxt_element

        
list = [19, 2, 31, 45, 30, 11, 121, 27]
insertionSort(list)
print(list)
