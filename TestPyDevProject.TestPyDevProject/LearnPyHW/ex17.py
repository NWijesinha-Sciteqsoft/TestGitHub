'''
Created on Oct 29, 2018

@author: nwijesinha

@change: This example is to copy file content to another file
'''
# import libraries
from sys import argv
from os.path import exists
from click._compat import raw_input


# Accept arguments from user to copy files and create objects for the files
script, from_file, to_file = argv

# inform user regarding copying files
print("Copying from %s to %s" % (from_file, to_file))

# We could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

# Print file size 
print("The input file is %d bytes long" % len(indata))

# check from use if the output file exists
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
raw_input("> ")

# copy file
out_file = open(to_file, 'w')
out_file.write(indata)

# inform the user of the file copy has been completed
print("Alright, all done.")
print("Hit RETURN to continue.")
raw_input("> ")

# close Files
out_file.close()
in_file.close()




