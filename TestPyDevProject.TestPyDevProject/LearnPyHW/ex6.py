'''
Created on Oct 18, 2018

@author: nwijesinha
'''
# Create a string variable x and assign a statement
x = "There are %d type of people" % 10
# Create string variable binary and assign binary
binary = "binary"
# Create string variable do not and assign don't
do_not = "don't"
# Create String variable y and assign a statement
y = "Those who know %s and those who %s" % (binary, do_not)

# print x and y
print(x)
print(y)

# Create variable hilariosu and assign False
hilarious = False
# Create a variable joke_evaluation and assign 'Isn't that joke so funny?
joke_evaluation = "Isn't that joek so funny?! %r"

# Print the the joke evaluation
print (joke_evaluation % hilarious)


'''
Create two variable to store a sentence and then print both variable together to show the sentence
'''
w = "This is the left sife of..."
e = "a string with a right side."

#Print the sentence
print(w + e)