'''
Created on Nov 29, 2018

@author: nwijesinha

This exercise to learn how to create deque using python

Deque or double ended queue has the featue of adding and removing elements from either end.
The deque module is part of the collection librar

'''
import collections as col


class Deque:

    # define the constructor for deque class
    def __init__(self, arrayval):
        self.deque = col.deque(arrayval) 
    
    # define add to right function for deque class    
    def addToRight(self, dataval):
        if dataval not in self.deque:
            self.deque.append(dataval)
            return True
        else:
            return False

    # define add to left function for deque class
    def addToLeft(self, dataval):
        if dataval not in self.deque:
            self.deque.appendleft(dataval)
            return True
        else:
            return False
    
    # define a function to check the deque size
    def dequeSize(self):
        return len(self.deque)
    
    # define a function to print the deque
    def printDeque(self):
        for i in self.deque:
            print(i)

    # define a function to remove an element from the right
    def removeFromRight(self):
        if len(self.deque) > 0:
            return self.deque.pop()
        return ("Err # 1001: element not found in the Deque")
    
    # define a function to remove an element from the elft
    def removeFromLeft(self):
        if len(self.deque) > 0:
            return self.deque.popleft()
        return ("Err # 1001: element not found in the Deque")
    
    # define a function to reverse the deque
    def reverseDequeu(self):
        self.deque.reverse()


# Array of values for the deque       
array = ['Mon', 'Tue', 'Wed']

# Create Dequeu
DoubelDeque = Deque(array)

# Print deque size
print("Printing Deque Size")
print(DoubelDeque.dequeSize())
print('*' * 30)

# Print deque
print("Printing the deque")
DoubelDeque.printDeque()
print('*' * 30)

# Add to left of deque
print("Adding to the left")
DoubelDeque.addToLeft("Sun")

# Print dequeu
print("Printing the deque")
DoubelDeque.printDeque()
print('*' * 30)

# Add to the right
print("Adding to the right")
DoubelDeque.addToRight("Thu")

# Print deque
print("Printing the deque")
DoubelDeque.printDeque()
print('*' * 30)

# Print the size of the deque
print("Printing Deque Size")
print(DoubelDeque.dequeSize())
print('*' * 30)

# Remove an element from the left of the dequeu
print("Remove from left")
print(DoubelDeque.removeFromLeft())
print("*" * 30)

# Print the deque
print("Printing the deque")
DoubelDeque.printDeque()
print('*' * 30)

# Remove an element from the right
print("Remove from Right")
print(DoubelDeque.removeFromRight())
print("*" * 30)

# Print the deque
print("Printing the deque")
DoubelDeque.printDeque()
print('*' * 30)

# Print the size of the deque
print("Printing Deque Size")
print(DoubelDeque.dequeSize())
print('*' * 30)

