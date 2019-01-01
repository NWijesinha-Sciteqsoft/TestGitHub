'''
Created on Nov 27, 2018

@author: nwijesinha

This exercise to learn how to create stacks in python
Stack:
Stack is similar to plates being stack on top of each other. The data elements are stack on top of each other.
Stack work on LIFO concept Last In Fir Out. In the Stack element inserted last is first out.
Stacks have push (adding) and pop (removing) functions

'''


# Create class stack
class Stack:

    # Define the constructor for stack
    def __init__(self):
        self.stack = []
 
     # Function to add an element to the stack       
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Function to remove an element from the stack
    def remove(self):
        if (len(self.stack)) <= 0:
            return("Stack is empty")
        else:
            # use the list pop method to remove an element
            return self.stack.pop()
    
    # Function to print the stack
    def stackPrint(self):
        for i in self.stack:
            print(i)
        print()

    # function to peek at the top of the stack
    def peek(self):
        if (len(self.stack)) <= 0:
            return("Stack is empty")
        else:
            # return the element at the top
            return self.stack[0]


AStack = Stack()
print("Peeking at the top of the stack")
print(AStack.peek())
print('*' * 40)
print('Adding values Mon, Tue, Wed to the stack')
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
print("Peeking at the top of the stack")
print(AStack.peek())
print('*' * 40)
print("Printing the stack")
AStack.stackPrint()
print('*' * 40)
print("Adding elements Thu and Fri")
AStack.add('Thu')
AStack.add('Fri')
print("Printing the stack")
AStack.stackPrint()
print('*' * 40)
print("Popping the last element entered from the stack")
print(AStack.remove())
print('*' * 40)
print("Printing the stack")
AStack.stackPrint()
print('*' * 40)
