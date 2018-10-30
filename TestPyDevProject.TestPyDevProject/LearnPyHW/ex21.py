'''
Created on Oct 30, 2018

@author: nwijesinha

This exercise is to show that functions can return variables

'''

# Define a function to add two variables
def add(a,b):
    print("ADDING %d + %d" % (a,b))
    return a + b

# Define a function to subtract two variables
def subtract(a,b):
    print("SUBRACTING %d - %d" % (a,b))
    return a-b
    
# Define a function to multiple two varibales
def multiply(a,b):
    print("MULTIPLYING %d * %d" % (a,b))
    return a*b

# Define a function to divide two variables
def divide(a,b):
    print("DIVIDE %d / %d" % (a,b))
    return a / b

# Print statement to inform the user 
print("Lets do some math with just functions!")

#define variable to use in the functions
age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# Print the values for age, height, weight and iq
print("Age: %d. height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# use the math function to received an answer for complex math
print("Here is a puzzel")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That become: ", what, "Can you do it by hand?" )

print("Here is a another puzzel")

this = add(24, subtract(divide(34, 100),1023))

print("Answer to this is", this)
        



