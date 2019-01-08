'''
Created on Jan 7, 2019

@author: nwijesinha

This exercise is to learn about searching a data structure in Python
Learn Search
In this type of search, a sequential search is made over all items one by one. 
Every item is checked and if a match is found then that particular item is returned, 
otherwise the search continues till the end of the data structure.

'''


def linear_search(input_list, search_for):
    search_at = 0
    search_res = False
    
    # Match the value with each data element
    while search_at < len(input_list) and search_res is False:
        if input_list[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res


l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 12))
print(linear_search(l, 91))
