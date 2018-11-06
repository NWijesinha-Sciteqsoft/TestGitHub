'''
Created on Nov 2, 2018

@author: nwijesinha

This exercise is to make decision using if then else statement

'''
# Import Python libraries to use
from click._compat import raw_input

# Print the prompt for users
print("You enter a dark room with two doors. Do you go through door #1 or door #2?")
# Declare the prompt for the user
prompt = "> "
# Declare the variable to capture user input
door = raw_input(prompt)

# Check user input against the decision. Check if the user entered 1
if door == "1":
    # print the next action to take to the user
    print("There is a giant bear here eating a cheese cake, What do you do?")
    print("Enter 1. Take the cake.")
    print("Enter 2. Scream at the bear.")
    # Declare a variable to capture the user input
    bear = raw_input(prompt)
    # Check if the user entered 1
    if bear == "1":
        #print the outcome
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        # Check if the user entered 2
        # Print the outcome
        print("The bear eats your face off. Good job!")
    else:
        # Check if the user entered anything other than 1 or 2
        # Print the outcome
        print("Well, doing %s is probably better. Bear runs away" % bear)

# Check user input against the decision. Check if the user entered 2
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("Enter 1. Blueberries.")
    print("Enter 2. Yellow jacket clothespins.")
    print("Enter 3. Understand revolvers yelling melodies.")
    
    # capture user input for next step
    insanity = raw_input(prompt)
    # Check if user input is 1 or 2
    if insanity == "1" or insanity == "2":
        # Print the outcome
        print("Your body survives powered by a mind of jello. Good Job!")
    else:
        #User input is 3 or anything else
        # Print the outcome
        print("The insanity rots your eyes into a pool of muck. Good job!")
else:
    # Check if the user entered anything other than 1 or 2
    # Print the outcome
    print("You stumble around and fall on knife and die. Good job!")