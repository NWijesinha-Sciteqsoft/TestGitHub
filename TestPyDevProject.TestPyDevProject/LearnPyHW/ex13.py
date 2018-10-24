'''
Created on Oct 23, 2018

@author: nwijesinha

This example is using alternative input method to pass a variable

'''

from sys import argv
from click._compat import raw_input
    
# Create variable for the example
script, first, second, third = argv

# using print method to assign information to variables
print("This script is called: ", script)
print("Your first variable is: ", first)
print("Your first variable is: ", second)
print("Your first variable is: ", third)

answer = raw_input("Did you see the correct out put?")

# Check fthe answer os Yes and print Yes or No
if answer == "Yes":
    print(answer)
else:
    print("No")