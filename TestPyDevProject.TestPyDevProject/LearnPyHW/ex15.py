'''
Created on Oct 25, 2018

@author: nwijesinha

This exercise is to read a text file 

'''

# Import sys.argument and click._compat.raw_input library
from sys import argv
from click._compat import raw_input

# Accept input from user for the filename
script, filename = argv

# Create File name object and hold the content in the file
txt = open(filename)
# print the file name
print("Here is your file %s:" % filename)
#Print the contents of the file
print(txt.read())

#request user to type the file name again
print("Type the filename again:")
#Prompt for input and save the file content to file_again variable
file_again = raw_input("> ")

# Print the content 
txt_again = open(file_again)
print(txt_again.read())




