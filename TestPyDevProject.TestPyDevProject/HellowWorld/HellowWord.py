'''
Created on Oct 15, 2017

@author: noel.wijesinha
'''

class HelloWorld:
    
    def __init__ (self, name):
        self.name = name
        
    def PrintHelloWorld(self):
        return self.name
    
helloworld_1 = HelloWorld("Ayubowan Lokaya!")
    
print(helloworld_1.PrintHelloWorld())