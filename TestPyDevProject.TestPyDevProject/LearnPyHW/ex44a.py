'''
Created on Nov 15, 2018

@author: nwijesinha

This exercise show how to do inheritance using a class

'''
class Parent(object):
    
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
