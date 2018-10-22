'''
Created on Oct 22, 2018

@author: nwijesinha

This example is to understand how to receive input from user using Python code

'''
from click._compat import raw_input

if __name__ == '__main__':
    # Ask the user for age and save in age variable
    print("How old are you?")
    age = raw_input()
    # Ask the user for the height and save in height variable
    print("How tall are you?")
    height = raw_input()
    # Ask the user for weight and save in weight variable
    print("How much do you weigh?")
    weight = raw_input()

    # Print the age, height and weight of the user
    print("So you're %r years old, %r cm tall and %r lbs heavy" % (age, height, weight))

