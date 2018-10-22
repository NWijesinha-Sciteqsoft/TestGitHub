'''
Created on Oct 22, 2018

@author: nwijesinha
'''
from click._compat import raw_input

if __name__ == '__main__':
    # Ask the user for age and save in age variable
    age = raw_input("How old are you? ")
    # Ask the user for the height and save in height variable
    height = raw_input("How tall are you? ")
    # Ask the user for weight and save in weight variable
    weight = raw_input("How much do you weigh? ")
    # Print the age, height and weight of the user
    print("So you're %r years old, %r cm tall and %r lbs heavy" % (age, height, weight))