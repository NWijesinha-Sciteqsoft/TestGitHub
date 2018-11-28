'''
Created on Nov 26, 2018

@author: nwijesinha

This exercise to learn how to create nodes in python

Nodes:
Nodes are pointers which has the data and pointer to the next location where data is stored in memory.
Nodes are created by implementing a class which hold the data and pointer

'''


# Create a node or pointer
# Implement a class for the node/pointer
class daynames:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

        
e1 = daynames("Mon")
e2 = daynames('Tue')
e3 = daynames("Wed")
e4 = daynames("Thu")

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

# Traversing the node elements
# Create an element and assign the first element in the node
thisvalue = e1
# Traverse the nodes and print out the elements in sequence the elements are linked
print("Printing the elements of the nodes")
while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval
    
