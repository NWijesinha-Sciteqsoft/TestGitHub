'''
Created on Oct 31, 2018

@author: nwijesinha

This module is for practicing Python Code
'''
# Example of how to print line with special characters, newlines and tabs
print("let's practice everything")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

# Variable that hold a paragraph with tabs, newlines and special characters
poem = '''
\tThe lovely world
with logic so firmly planed
cannot discern \n the needs of love
nor comprehend passion from intuition
\n\t\twhere there is none.
'''
# Print the poem with borders 
print("---------------")
print(poem)
print("---------------")

# doing math and printing math answer
five = 10-2+3-6
print("This should be five: %s" % five)

# Create a math function to complete math equations and return multiple values
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Execute the math function
start_point = 10000
# assign values returned from math function to three variables
beans, jars, crates = secret_formula(start_point)

# Print the values
print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars and %d crates." % (beans, jars, crates))

# Another example of executing the math value directly using the print
start_point = start_point / 10
print("We can also do that this way:")
print("We'd have %d beans, %d jars and %d crates." % secret_formula(start_point))

