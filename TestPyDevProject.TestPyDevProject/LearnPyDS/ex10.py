'''
Created on Nov 27, 2018

@author: nwijesinha

This exercise to learn how to create a link lists in python
LinkList
A link lists is a sequence of data elements which are connected together via a link.
Each data element contains a connection to another data element in form of a pointer
Python does not have link lists in its standard library.
We implement a link list in python by using concepts of nodes

'''


# Create a class for the node
class Node(object):

    # constructor for Node class
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

        
class SLinkList(Node):

    # constructor for SLinkList class
    def __init__(self):
        self.headval = None
    
    # define list print function
    def listprint(self):
        # assign heaval to printval
        printval = self.headval
        while printval is not None:  # iterate while printval is not empty
            print(printval.dataval)  # print element
            printval = printval.nextval  # assign pointer location to next element to printval
    
    # Function to add a node at the begining
    def AtBegining(self, newdata):
        # Create new node
        NewNode = Node(newdata)
        
        # update the new nodes next val to existing node
        NewNode.nextval = self.headval
        
        # Link the new node
        self.headval = NewNode
    
    # Function to add a node to the end
    def AtEnd(self, newdata):
        # Create new node
        NewNode = Node(newdata)
        
        # Link the new node
        if self.headval is None:  # check if head value is none
            self.headval = NewNode  # assign pointer to new node to head value
            return  # end function
        
        laste = self.headval  # assign head value to last element
        while(laste.nextval):  # loop through while there is next ValueError
            laste = laste.nextval  # assign next value to last element
            
        laste.nextval = NewNode  # link the node at the end

    # Function to add a node between two nodes
    def InBetween(self, middle_node, newdata):
        if middle_node is None:  # middle node is not found
            print("The mentioned node is not found!")  # Print error message
            return  # end function
        # if middle node is found
        NewNode = Node(newdata)  # create a new node
        NewNode.nextval = middle_node.nextval  # assign the middle node next value to new node next value
        middle_node.nextval = NewNode  # assign new node to middle node next value
        
    # Function to remove a node
    def RemoveNode(self, RemoveKey):
        # Create variable to hold head value
        HeadVal = self.headval
        # Check if head value is not empty
        if (HeadVal is not None):
            # check if head value data value is equal to remove key
            if (HeadVal.dataval == RemoveKey):
                # assign pointer to self
                self.headval = HeadVal.nextval
                # assign None to head value attribute
                HeadVal = None
                return  # stop the function
        # Check if head value is not empty    
        while(HeadVal is not None):
            # check if data value in node is same as remove key
            if HeadVal.dataval == RemoveKey:
                break  # exit function
            prev = HeadVal  # assign head value to prvious
            HeadVal = HeadVal.nextval  # assign next node pointer to HeadValue
        # Check if HeavVal is empty then stop function            
        if (HeadVal == None):
            return
        # assign next location pointer to previous 
        prev.nextval = HeadVal.nextval
        HeadVal = None  # empty head value

        
# Define a link list using SlinkList Class
list1 = SLinkList()
# Add the head value for list1 linklist
list1.headval = Node("Mon")
# create nodes e2 and e3 which contain elements Tue and Wed 
e2 = Node('Tue')
e3 = Node('Thu')
# Link first node to the second node
list1.headval.nextval = e2

# link second node to third node
e2.nextval = e3

# Print the Link list
print("Printing the current element in link list")
list1.listprint()

# Adding an element to the begining of the link list
print("Adding an element to begining of the link list")
list1.AtBegining("Sun")

# Print the Link list
print("Printing the current element in link list")
list1.listprint()

# Adding an element to the end of the link list
print("Adding an element to begining of the link list")
list1.AtEnd("Fri")

# Print the Link list
print("Printing the current element in link list")
list1.listprint()

# adding node between nodes
list1.InBetween(list1.headval.nextval, 'Wed')

# Print the Link list
print("Printing the current element in link list")
list1.listprint()

# Remove Wed from link list
list1.RemoveNode('Wed')

# Print the Link list
print("Printing the current element in link list")
list1.listprint()
