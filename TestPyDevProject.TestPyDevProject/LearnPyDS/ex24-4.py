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

Shell Sort involves sorting elements which are away from each other. 
We sort a large sublist of a given list and go on reducing the size of the list until all elements are sorted.

'''


def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            # sort the sub list for this gap
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap
                input_list[j] = temp
        # reduce the gap for next element
        gap = gap // 2

        
list = [19, 2, 31, 45, 30, 11, 121, 27]
shellSort(list)
print(list)
