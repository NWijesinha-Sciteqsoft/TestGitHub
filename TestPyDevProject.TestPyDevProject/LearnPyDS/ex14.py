'''
Created on Nov 29, 2018

@author: nwijesinha

This exercise is learn how to create advanced linked list
Advance Linked list or double linked list have a element which has pointer to next element and previous element.
Doubled linked list contains a link element called first and last
The last link has null to mark the end of the list

'''
from platform import node
from pandas.io.formats import printing
from tkinter.constants import LAST


class Node:

    # constructor for Node class
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None
        self.prevval = None

    
class DoubeLinkList:

    # constructor for Double Link List class
    def __init__(self):
        self.head = None
    
    # define a function to add an element to the link list
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.nextval = self.head
        if self.head is not None:
            self.head.prevval = NewNode
        self.head = NewNode
    
    # print function for double linked list
    def printList(self, node):
        while (node is not None):
            print(node.dataval)
            # last = node
            node = node.nextval
            
    # define a function to check the list size
    def listSize(self, node):
        count = 0
        while (node is not None):
            count += 1
            # last = node
            node = node.nextval
        return count
    
    # define insert function for link list
    def insert(self, PrevNode, NewVal):
        if PrevNode is None:
            # if previous Node is not there
            return False  # return false
        # Create a new node and add element
        NewNode = Node(NewVal)
        # assign previous node nextval to newnode nextval
        NewNode.nextval = PrevNode.nextval
        # assign newnode to previous node nextval
        PrevNode.nextval = NewNode
        # assign previous node to newnode prevval
        NewNode.prevval = PrevNode
        
        if NewNode.nextval is not None:
            # check if newnode nextval not empty
            NewNode.nextval.prevval = NewNode  # assign NewNode to NewNode newval prevval
            
    # Define append function
    def append(self, NewVal):
        # Create a new node and insert element to the new node
        NewNode = Node(NewVal)
        # Assign next value in the New Node to None
        NewNode.nextval = None
        # Check is head pointer is none
        if self.head is None:
            # Assign the prevous value of New Node to None
            NewNode.prevval = None
            # Point the head pointer to New Node
            self.head = NewNode
            # End function
            return
        # Asign pointer in head to last
        last = self.head
        # While next value is not None
        while(last.nextval is not None):
            # Loop through and assign the value to last
            last = last.nextval
        # Point next value pointer to New node
        last.nextval = NewNode
        # Point New Node prev value to last
        NewNode.prevval = last 
        return
             

DLList = DoubeLinkList()
print("Double Link List size: ", DLList.listSize(DLList.head))
print('*' * 20)
DLList.push(12)
DLList.push(8)
DLList.push(62)
print("Printing Link List elements")
DLList.printList(DLList.head)
print('*' * 20)
print("Double Link List size: ", DLList.listSize(DLList.head))
print('*' * 20)
DLList.insert(DLList.head.nextval, 13)
print("Printing Link List elements")
DLList.printList(DLList.head)
print('*' * 20)
print("Double Link List size: ", DLList.listSize(DLList.head))
print('*' * 20)
DLList.append(45)
print("Printing Link List elements")
DLList.printList(DLList.head)
print('*' * 20)
print("Double Link List size: ", DLList.listSize(DLList.head))
print('*' * 20)
        
