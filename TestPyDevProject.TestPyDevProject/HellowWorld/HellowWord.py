'''
Created on Oct 15, 2017

@author: noel.wijesinha
@title: Hello World Test Application
@description: This class will create hello world object and print the hello word on the screen
'''

class HelloWorld:
    
    def __init__ (self, name):
        self.name = name
        
    def PrintHelloWorld(self):
        return self.name
    
helloworld_1 = HelloWorld("Hello World!")
    
print(helloworld_1.PrintHelloWorld())