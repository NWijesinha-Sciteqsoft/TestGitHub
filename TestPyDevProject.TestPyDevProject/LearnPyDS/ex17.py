'''
Created on Dec 20, 2018

@author: nwijesinha

'''


class Node:

    # Define constructor for class
    def __init__(self, data):
        # Create variables for left value, right value and data
        self.leftval = None
        self.rightval = None
        self.data = data
        
    # Define insert to create nodes
    def insert(self, data):
        # check if there is a value in data in the node
        if self.data:
            # check if data passed is less than node data value
            if data < self.data:
                if self.leftval is None:
                    # Node left value is empty create a new node with data and assign the pointer to the new node into left value
                    self.leftval = Node(data)
                else:
                    # If not pass the data back into insert function
                    self.leftval.insert(data)
            # check if data passed is greater than node data value
            elif data > self.data:
                # Node right value is empty, create a new node with data and assign the pointer to the new node into left value
                if self.rightval is None:
                    self.rightval = Node(data)
                else:
                    # If not pass the data back into insert function
                    self.rightval.insert(data)
        else:
            # Node does not have data assign the data to node data value
            self.data = data
                  
    # Define find value method to compare the value with nodes
    def findVal(self, lkpval):
        # check lookup value is less than node data value
        if lkpval < self.data:
            # Left value is empty return the lookup value with Not Found message
            if self.leftval is None:
                return str(lkpval) + " Not Found" 
            # if not search the left side of the tree
            return self.leftval.findVal(lkpval)
        elif lkpval > self.data:
            # check lookup value is greater than node data value
            if self.rightval is None:
                 # right value is empty return the lookup value with Not Found message
                return str(lkpval) + " Not Found"
            # if not search the right side of the tree
            return self.rightval.findVal(lkpval)
        else: 
            # value is found pass the data with found message
            print(str(self.data) + ' is found') 
    
    # Define print tree function
    def printTree(self):
        if self.leftval:
            # print the left side of the tree       
            self.leftval.printTree()
        print(self.data),
        if self.rightval:
            # print the right side of the tree
            self.rightval.printTree()

        
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()
print(root.findVal(7))
print(root.findVal(14))    
