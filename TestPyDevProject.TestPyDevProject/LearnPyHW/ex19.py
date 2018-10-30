'''
Created on Oct 30, 2018

@author: nwijesinha

This exercise shows how to call a function and pass variables
'''
# Define a function to print the count of cheeses and count of boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Calling function by directly passing the arguments
print("We can just give the function number directly")
cheese_and_crackers(20, 30)

# Calling function by passing variables as arguments which contain values
# define variables and assign values
print("OR, we can use variable from our script")
amount_of_cheese = 10
amount_of_crackers = 50
# Call the function and pass the variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calling a function directly and by passing a math arguments
print("We can even do math inside")
cheese_and_crackers(10 + 20, 5 + 6)

# Calling function by passing variables as arguments which contain values and completing math
print("And we can combine the two variables and math inside")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)





