'''
Created on Oct 30, 2018

@author: nwijesinha

This exercise is to show Python Names, Variable, and Functions
'''

'''
Create an function that accepts multiple argument and assign it to two variables
This function is like a scrip with argv
'''
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg3: %r" % (arg1, arg2))
 
 # creating a function that accepts only two arguments and assign to two variables   
def print_two_again(arg1, arg2):
    print("arg1: %r, arg3: %r" % (arg1, arg2))

def print_one(arg1):
    print("arg1: %r" % arg1)    
    
# creating a function with no arguments
def print_nothing():
    print("I got nothing")    


# call the functions
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("Zed")
print_nothing()



