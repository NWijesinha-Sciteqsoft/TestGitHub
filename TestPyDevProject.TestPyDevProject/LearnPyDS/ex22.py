'''
Created on Jan 2, 2019

@author: nwijesinha

This exercise is to create a function for backtracking in python
backtracking is a form of recursion, but it involves choosing only option out of any possibilties

'''


# define a function for backtracking
def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x 
                for y in permute(1, s)
                for x in permute(list - 1, s)
                ]


s = ["a", "b", "c"]

print(permute(1, s))
print(permute(2, s))
