'''
Created on Dec 18, 2018

@author: nwijesinha

This exercise is to create a tree or binary tree using Python
Tree is a node connected by the edges.
Tree is nonlinear data structure with the following properties
- One node is marked as Root node
- Other than the Root node, every other node has one parent
- Each node can have an arbitrary number of child nodes

'''


class Node:

    # Define constructor for the class
    def __init__(self, data):
        # Define values for left value, right value and data to hold the data
        self.leftval = None
        self.rightval = None
        self.data = data
        
    def insert(self, data):
        # Compare the new value with parent node
        if self.data:
            # If parent node has a value
            if data < self.data:
                # If the value is less than parent node value
                if self.leftval is None:
                    # if left value is empty then create a new node add a point to the new node
                    self.leftval = Node(data)
                else:
                    # else insert the data
                    self.leftval.insert(data)
            elif data > self.data:
                # Compare the the new value is greater than parent node data
                if self.rightval is None:
                    # if the right value in the parent node is empty create a new node with value and add the point to the new node
                    self.rightval = Node(data)
                else:
                    # else insert the data 
                    self.rightval.insert(data)
        else:
            # if the parent value does not have data then assign the new value to parent
            self.data = data
        
    # Define function to print the tree
    def printTree(self):
        # print the data in the tree
        if self.leftval:
            self.leftval.printTree()
        print(self.data),
        if self.rightval:
            self.rightval.printTree()

        
# Create Tree with root node
root = Node(12)
# Insert 6, 14, 3 to the tree
root.insert(6)
root.insert(14)
root.insert(3)
# Print the tree
root.printTree()
        
