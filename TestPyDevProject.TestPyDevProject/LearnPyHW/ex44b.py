'''
Created on Nov 15, 2018

@author: nwijesinha

This exercise show how to override a function of parent class when doing in inheritance in python
'''

class Parent(object):
    
    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
