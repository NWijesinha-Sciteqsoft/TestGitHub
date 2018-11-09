'''
Created on Nov 9, 2018

@author: nwijesinha

This exercise to make game using if-statments for-loops and while-lopps

'''
# Import libraries
from sys import exit
from click._compat import raw_input

# Define a function for dead which print the statement passed to the function and exit the game
def dead(why):
    print(why, "Good job!") # print statement
    exit(0) # exit program

# Define a function for Gold room
def gold_room():
    # Print direction for user
    print("This room is full of gold. How much do you take?")
    # Capture user input and save in variable
    next = raw_input("> ")
    if "0" in next or "1" in next: # Check if user in put is 0 or 1
        how_much = int(next) # convert user input to integer and save in variable
    else:
        dead("Man, learn to type a number.") # else print statement calling dead function
        
    # Check how much of gold user wants
    if how_much < 50: # check if user input is less than 50
        print("Nice, you're not greedy, you win!") # print statement
        exit(0) # exit program
    else:
        dead("You greedy bastard!") # if user input over 50 then print statement calling dead function

# Define bear_room function
def bear_room():
   # Print instructions to the user
    print(" There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    # Set variable to false
    bear_moved = False
    
    # Loop through and capture use input
    while True:
        next = raw_input("> ") # Accept user input
        
        if next == "take honey": # check if user input is take honey
            dead("The bear looks at you then slaps your face off.") # print statement by calling dead function
        elif next == "taunt bear" and not bear_moved: # Check if user input it taint bear and bear moved
            print("The bear has moved from the door, You can go through it now.") # Print statement
            bear_moved = True # set bear moved variable to true
        elif next == "taunt bear" and bear_moved: # Check if user input it taint bear and bear moved
            dead("The bear gets pissed off at you and chews your face off.") # print statement by calling dead function
        elif next == "open door" and bear_moved: # Check if user input it open door and bear moved
            gold_room() # call gold_room function
        else:
            print("I got no idea what that means.") # if other input print statment

# Define cthulhu_room function
def cthulhu_room():
    # Print instructions to the user
    print("Here you see the great evil Cthulhu.")
    print("He, it, wahtever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    next = raw_input("> ")  # Accept user input
    
    if "flee" in next: # Check if user input is flee
        start() # call start function
    elif "head" in next: # Check if user input is head
        dead("Well that was tasty!") # print statement by calling dead function
    else:
        cthulhu_room() # if any pther input call cthulhu_room function

# Define Start function
def start():
    # Print the instructions to the user
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    # Accept user input
    next = raw_input("> ")
    
    if next == "left": # Check if user input is left
        bear_room() # Call bear room function
    elif next =="right": # Check if user input is right
        cthulhu_room() # Call cathulhu room function
    else:
        dead("You stumble around the room until you starve.") # if any other input call function dead to print statement


start()
     