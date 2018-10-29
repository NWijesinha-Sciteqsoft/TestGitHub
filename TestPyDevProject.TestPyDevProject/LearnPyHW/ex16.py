'''
Created on Oct 29, 2018

@author: nwijesinha

This exercise is to read and write files

'''
# Import libraries
from sys import argv
from click._compat import raw_input


# Caoture and assign file name to variable from user
script, filename = argv

# promt the user regarding action

print("We are going to erase %r." % filename)
print("If you dont want that, hit CRTL-C (^C).")
print("If you do want that, enter RETURN.")
raw_input("?")

# Read fiel
print("Opening the file....")
txt = open(filename, 'w')

# Erase the file
print("Truncating the file. Goodbye!")
txt.truncate()

# Prompt user for three line to write to the file
print(" Now I am going to ask you for three lines.")

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

# Inform the user that lines are being written to the file
# Write line 1 to file
txt.write(line1)
txt.write("\n")
# Write line 2 to file
txt.write(line2)
txt.write("\n")
# Write line 3 to file
txt.write(line3)
txt.write("\n")

#close the file
print("And finally now we are going to close the file.")
txt.close()



