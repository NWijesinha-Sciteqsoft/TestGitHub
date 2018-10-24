'''
Created on Oct 24, 2018

@author: nwijesinha
'''

# Import Sys.argument library
from sys import argv

# assign arguments when script is run to script, username
script, username = argv
# Create variable prompt
prompt = '>'

# Print the arguments collected and prompt the user for input
print("Hi %s, I'm the %s script.", % (username, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s", % username)
