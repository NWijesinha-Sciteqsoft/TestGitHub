'''
Created on Nov 6, 2018

@author: nwijesinha

This exercise to learn while loop in python

'''
from lib2to3.fixer_util import Number

# Declare variable for the loop condition and declare list
i = 0
numbers = []
condition = 10
increment = 2

'''
Loop through as long as i is less than 10 and add i to numbers then increment i by 1

'''
while i < condition:
    print("At the top i is %d:" % i) # Print i when entering loop
    numbers.append(i) # Add i to list
    i = i + increment # increment i by 1
    print("Numbers now: ", numbers) # Print the list
    print("At the bottom i is %d:" % i) # Print value of i after increment


# Print heading
print("The numbers: ")

# Print the numbers in the list
for num in numbers:
    print(num)
