'''
Created on Nov 20, 2018

@author: nwijesinha

This exercise is to work with Tuple in Python
Tupl:
A Tuple is a sequence of immutable Python objects. 
Tuples are sequences, just like lists. 
The difference between tuples and lists are, 
the tuples cannot be changes unlike lists and tuple use parentheses, 
where as lists use square brackets.

'''

# Define tuple for use in the exercise
tuple1 = ("physics", 'chemistry', 1997, 200)
tuple2 = (1, 2, 3, 4, 5)
tuple3 = "a", "b", 'c', 'd'

# Accessing tuple values 
print("Printing tuple 1 values")
for i in range(len(tuple1)):
    print("Tupel1[%i]" % i, tuple1[i])

print("Printing tuple 2 values")
for j in range(len(tuple2)):
    print("Tupel2[%i]" % j, tuple2[j])
    
print("Printing tuple 3 values")
for k in range(len(tuple3)):
    print("Tupel3[%i]" % k, tuple3[k])

# accessing tuple by index and index range
print("Tuple 1 index 2 value is: ", tuple1[2])
print("tupe2[1:5] is: ", tuple2[1:5])

# Creating tuple of existing tuples
# Define tuples
tuple4 = (12, 34.56)
tuple5 = ('abc', 'xyx')
print("Printing tuple 4", tuple4)
print("Printing tuple 5", tuple5)
# Create a new tuple from existing tuples
tuple6 = tuple4 + tuple5
print("Printing tuple 6", tuple6)

# deleting tuple
tuple7 = tuple1
print("before printing tuple 7", tuple7)
del tuple7
print("after deleting tuple 7", tuple7)

    