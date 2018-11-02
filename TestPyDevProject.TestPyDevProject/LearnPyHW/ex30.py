'''
Created on Nov 2, 2018

@author: nwijesinha

This exercise is to practice if then else

'''

# Declare variables for the exercise
people = 30
cars = 40
buses = 15

# if then else example 1
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
    
# if then else example 2
if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take buses.")
else:
    print("We still can't decide.")
    
# if the else example 3
if people > buses:
    print("Alright, lets just take the buses.")
else:
    print("fine, let's stay home then.")