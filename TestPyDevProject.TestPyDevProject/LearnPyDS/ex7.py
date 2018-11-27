'''
Created on Nov 26, 2018

@author: nwijesinha

This exercise is learn sets in python
Sets
The sets in python are typically used for mathematical operations like union, intersection, difference and complement etc.
We can create a set, access it's element and carry out these mathematical operations as show below. The has the following condistions
The elements in the set cannot be duplicates
The elements in the set are immutable (cannot be modified) but the set as a while mutable.
There is no index attached to any element in a python set

'''

# Creating a set using set() function
Days = set(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
Months = set(["Jan", "Feb", "Mar"])
Dates = set([21, 22, 17])
# Print sets
print("Printing sets")
print(Days)
print(Months)
print(Dates)
print("*"* 50)

# Accessing values in a set using a loop
for i in Days:
    print(i)
print("*"* 50)

# Adding a element to a set
Days1 = Days
print("Printing set before adding")
for i in Days1:
    print(i)
print("*"* 50)
# Updating the Days1 with Sunday
Days1.add('Sun')
print("Printing set after adding")
for i in Days1:
    print(i)
print("*"* 50)

# Removing a element to a set
Days2 = Days1
# Days2.add('Sun')
print("Printing set before removing")
for i in Days2:
    print(i)
print("*"* 50)
# Updating the Days1 with Sunday
Days2.discard('Sun')
print("Printing set after adding")
for i in Days2:
    print(i)
print("*"* 50)

# Using the union operation on two sets to produce a new set containing all distinct elements
# Create two set to contain days of the week
DaysA = set(["Mon", 'Tue', 'Wed'])
DaysB = set(["Wed", 'Thu', 'Fri', 'Sat', 'Sun'])
# Create a union of DaysA and DaysB
AllDays = DaysA | DaysB
# print the new set with union of the two sets with all distinct elements
print("Printing Union of Sets")
print(AllDays)
print("*"*50)

# Using the intersection operation on two sets to produce a new set containing only common elements
# Create two set to contain days of the week
DaysA = set(["Mon", 'Tue', 'Wed'])
DaysB = set(["Wed", 'Thu', 'Fri', 'Sat', 'Sun'])
# Create a union of DaysA and DaysB
AllDays = DaysA & DaysB
# print the new set with union of the two sets with all distinct elements
print("Printing Intersection of Sets")
print(AllDays)
print("*"*50)

# Using difference function on two sets produce a new set with only the elements from the first set a none from the second set
# Create two set to contain days of the week
DaysA = set(["Mon", 'Tue', 'Wed'])
DaysB = set(["Wed", 'Thu', 'Fri', 'Sat', 'Sun'])
# Create a difference of DaysA and DaysB
AllDays = DaysA - DaysB
# print the new set with union of the two sets with all distinct elements
print("Printing difference of Sets")
print(AllDays)
print("*"*50)

# Using compare set to compare if the set are identical
# Create two set to contain days of the week
DaysA = set(["Mon", 'Tue', 'Wed'])
DaysB = set(["Mon", 'Tue', "Wed", 'Thu', 'Fri', 'Sat', 'Sun'])
# Create a difference of DaysA and DaysB
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
# print the new set with union of the two sets with all distinct elements
print("Printing if set A is subset of B")
print(SubsetRes)
print("Printing if set B is superset of A")
print(SupersetRes)
print("*"*50)

