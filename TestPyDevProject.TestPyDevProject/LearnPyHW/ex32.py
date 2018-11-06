'''
Created on Nov 6, 2018

@author: nwijesinha

This exercise work with loops and list using Python

'''

# Declare lists
# List for count
the_count = [1, 2, 3, 4, 5] 
# List for fruits
fruits = ['apples', 'oranges', 'pears', 'apricots']
# List for money 
change = [1, 'pennies', 2, 'dime', 3, 'quarters']

# This part of the program goes through list of counts and prints the number
for number in the_count:
    print("This is count %d" % number)
    
# This part of the program goes through the list of fruits and print the fruit
for fruit in fruits:
    print("A fruit of type: %s" % fruit)
    
# This part of the code goes through a mixed list of string and integers
for i in change:
    print("I got %r" % i)
    
# Declare a list
elements = []

# This part of the code use the range function to do 0 to 5 count
for i in range(0, 5):
    print("Adding %d to the list." % i)
    # Assign the value using append which is function of lists
    elements.append(i)
    
# Print the list to check if the values were assigned
for i in elements:
    print("Element was: %d" % i)
    
# Declare two dimension list
twodimension_lists = [[1,2,3],[4,5,6]]

T = twodimension_lists

# print the list
print(type(twodimension_lists))
    
for i in T:
    for j in i:   
        print(j, end = " ")
        print()
        
        


         