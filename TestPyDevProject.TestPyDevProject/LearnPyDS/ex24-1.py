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

This exercise is to create a bubble sort algorithm
Bubble Sort is a comparison-based algorithm in which each pair of adjacent elements is compared 
and the elements are swapped if they are not in order.
'''


class Sort:
    
    # define constructor
    def __init__(self, list):
        self.list = list
        self.temp = None
        
    # function for bubble sort
    def bubbleSort(self):
        for iter_num in range(len(self.list)):
            # iterate through the list
            for idx in range(iter_num):
                # iterate through the index
                if self.list[idx] > self.list[idx + 1]:
                    self.temp = self.list[idx]
                    self.list[idx] = self.list[idx + 1]
                    self.list[idx + 1] = self.temp
      
    def printList(self):
         for idx in self.list:
            print (idx)

                
list = [19, 2, 31, 45, 6, 11, 121, 27] 
sort_list = Sort(list)
print('Print list before sorting')
sort_list.printList()
print('*' * 20)
print('Applying bubble sort')
sort_list.bubbleSort()
print('Print list befor sorting')
sort_list.printList()
print('*' * 20)
