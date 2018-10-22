'''
Created on Oct 22, 2018

@author: nwijesinha

This example looks at using \ and using escape sequences for different characters within strings variables

'''
# Create string variable tabby_cat and assign escape sequence with statement
tabby_cat = "\tI'm tabbed in." 
# Create string variable persian_cat and assign escape sequence with statement
persian_cat = "I'm split\non a line."
# Create string variable backslash_cat and assign escape sequence with statement
blackslash_cat = "I'm \\ a \\ cat"

# Create string variable fat_cat and assign escape sequence with statement
fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# Print variable to check the statements
print(tabby_cat)
print(persian_cat)
print(blackslash_cat)
print(fat_cat)

'''
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i),
'''