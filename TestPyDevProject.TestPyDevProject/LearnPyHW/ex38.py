'''
Created on Nov 9, 2018

@author: nwijesinha

This exercise used mixes string and list for all kinds of fun things

'''

# Declare variable to hold ten things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# Print statement
print("Wait there's not 10 things in the that list, lets fix that.")

# Declare variable stuff and assign ten things by add space
stuff = ten_things.split(' ')
# Declare a list
more_stuff = ["Day", "Night", "Songs", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# Loop through as long as stuff does not containt 10
while len(stuff) != 10:
    # assign the item from more stuff to next one
    next_one = more_stuff.pop()
    # Print statement
    print("Adding: ", next_one)
    # Add thing to stff
    stuff.append(next_one)
    print("There's %d item now." % len(stuff)) # Print the number of items in stuff

# Print stuff
print("There we go: ", stuff)

# Print statement
print("Let's do some thonsg with stuff.")

print(stuff[1]) # print thing in position 1
print(stuff[-1]) # print the thing in the last position
print (stuff.pop()) # prints the thing in the last position
print(' '.join(stuff)) # print thing in stuff with spaces
print('#'.join(stuff[3:5])) # print things in position 3 and 4 with # pound

