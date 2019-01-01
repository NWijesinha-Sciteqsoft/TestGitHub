'''
Created on Nov 28, 2018

@author: nwijesinha

This exercise is to learn how to create queue using python

Queue is similar to a queue at the bank to deposit money at a teller. 
The queue in python the data elements are stacked like stack but work on FIFO.
different between queue and stack is that stack is a array and queue is a list
First in First out; the element which is in the queue is removed first

'''


# define class queue
class Queue:

    # define the constructor for class queue
    def __init__(self):
        self.queue = list()
        
    def addToQueue(self, dataval):
        # Inser method to add an element to the queue
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        else:
            return False

    # define a function to return the size of the queue
    def queueSize(self):
        return len(self.queue)
    
    # define a function to print the queue
    def printQueue(self):
            for i in self.queue:
                print(i)
    
    # Remove function for the queue
    def removeFromQueue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return ("Err # 1001: No element found in the Queue")

    
TheQueue = Queue()
TheQueue.addToQueue('Mon')
TheQueue.addToQueue('Tue')
print("Printing the size of the Queue")
print(TheQueue.queueSize())
print('*' * 30)
print("Printing the Queue")
TheQueue.printQueue()
print('*' * 30)
TheQueue.addToQueue('Wed')
TheQueue.addToQueue('Thu')
TheQueue.addToQueue('Fri')
TheQueue.addToQueue('Sat')
TheQueue.addToQueue('Mon')
TheQueue.addToQueue('Sun')
print("Printing the size of the Queue")
print(TheQueue.queueSize())
print('*' * 30)
print("Printing the Queue")
TheQueue.printQueue()
print('*' * 30)
TheQueue.removeFromQueue()
print("Printing the size of the Queue")
print(TheQueue.queueSize())
print('*' * 30)
print("Printing the Queue")
TheQueue.printQueue()
print('*' * 30)
