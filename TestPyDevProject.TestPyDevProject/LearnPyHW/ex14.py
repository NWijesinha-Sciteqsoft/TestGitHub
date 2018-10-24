'''
Created on Oct 24, 2018

@author: nwijesinha
'''

# Import Sys.argument library
from sys import argv
from click._compat import raw_input

# assign arguments when script is run to script, username
script, user_name = argv
# Create variable prompt
prompt = '>'

# Print the arguments collected and prompt the user for input
print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s" % user_name)
likes = raw_input(prompt)

# Accept second input from user
print("Where do you live %s?" % user_name)
lives = raw_input(prompt)

# Accept third input from user
print("What kind of computer do you have?")
computer = raw_input(prompt)

# Prin the user input on the screen
print("""
Alright, so you have said %r about liking me
You live in %r. Not sure where that is.
And you have a %r computer. Nice

""" % (likes, lives, computer))