'''
Created on Nov 19, 2018

@author: nwijesinha
'''

class Parent(object):
    # Parent class
    
    def override(self):
        # Override function which prints "PARENT override()"
        print("PARENT override()")

    def implicit(self):
        # Implicit function which prints "PARENT implicit()"
        print("PARENT implicit()")
        
    def altered(self):
        # Altered function which prints "PARENT altered()"
        print("PARENT altered()")
        
class Child(Parent):
    # Child class
    def override(self):
        # Override function which override the parent override function and prints "CHILD override()"
        print("CHILD override()")
    
    def altered(self):
        # Altered function which over ride parents altered function prints "CHILD altered()"
        print("CHILD, BEFORE PARENT altered()")
        # Reset Parent altered function which prints "PARENT altered()"
        super(Child, self).altered()
        # Print the state of the altered function
        print("CHILD, AFTER PARENT altered()")
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

'''
dad.altered()
son.altered()
'''