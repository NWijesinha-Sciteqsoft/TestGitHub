'''
Created on Oct 30, 2018

@author: nwijesinha
'''
# Import libraries for the solution
from sys import argv

# Accept file name from user through command line
script, input_file = argv

# Define a function to print file that is passed as an argument
def print_all(f):
    print (f.read())
    
# Define a function rewind passing file as argument
def rewind(f):
    f.seek(0)
    
# Define a function to print a line in the file passing line count and file as arguments
def print_a_line(line_count, f):
    print("Line %d is %s" % (line_count, f.readline()))


# create an object to hold the file
current_file = open(input_file)
print_all(current_file)

# Refind the file using the file
print("Now let's rewind, kind of like a tape")
rewind(current_file)

# Print three line from the file
print("let's print three line")
current_line = 1
# Print the first line
print_a_line(current_line, current_file)
# Print the next line
current_line += current_line 
print_a_line(current_line, current_file)
#Print the next line
current_line += current_line
print_a_line(current_line, current_file)




