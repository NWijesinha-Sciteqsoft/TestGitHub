'''
Created on Oct 22, 2018

@author: nwijesinha
'''
# Create variable formatter and assign 4 formatters to the variables
formatter = "%r %r %r %r"

# Print 1 2 3 4 using the formatter variables
print(formatter % (1,2,3,4))
# Print 1 2 3 4 in word form using the formatter variables
print(formatter % ("one", "two", 'three', 'four'))
# Print True and False using the formatter variables
print(formatter % (True, False, False, True))
# Print formatter using the formatter variables
print(formatter % (formatter, formatter, formatter, formatter))
# Print a phrase using the formatter variable
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.")
)


