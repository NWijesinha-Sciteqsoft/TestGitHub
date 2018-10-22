'''
Created on Oct 22, 2018

@author: nwijesinha

This example is to understand how to receive input from user using Python code

'''
from click._compat import raw_input

if __name__ == '__main__':
    print("How old are you?")
    age = raw_input()
    print("How tall are you?")
    height = raw_input()
    print("How much do you weigh?")
    weight = raw_input()

print("So you're %r years old, %r cm tall and %r lbs heavy" % (age, height, weight))

