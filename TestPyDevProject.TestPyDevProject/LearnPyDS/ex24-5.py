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

Selection Sort
In selection sort we start by finding the minimum value in a given list and move it to a sorted list. 
Then we repeat the process for each of the remaining elements in the unsorted list. 
The next element entering the sorted list is compared with the existing elements and placed at its correct position.

'''


def selectionSort(input_list):
    
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(idx + 1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j 
        # swap the minimum value with the compared value
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

                                                          
l = [19, 2, 31, 45, 30, 11, 121, 27]
selectionSort(l)
print(l)
