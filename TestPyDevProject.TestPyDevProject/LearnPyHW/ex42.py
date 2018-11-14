'''
Created on Nov 14, 2018

@author: nwijesinha

This exercise is to create class in python

'''

## Create a class for animal
class Animal(object):
    pass

# create dog class by extending the animal class
class Dog(Animal):
    
    def __init__(self, name):
        # variable to store name of dog
        self.name = name

# create cat class by extending the animal class
class Cat(Animal):
    
    def __init__(self, name):
        # variable to store name of cat
        self.name = name
        
## Create a class for Person
class Person(object):
    
    def __init__(self, name):
        # variable to store the persons name
        self.name = name 
        # variable to store the person's pet
        self.pet = None
        
 ## Create a class for Employee by extending the person class
class Employee(Person):
    
    def __init__(self, name, salary):
        #create an instance of the person object and assign the name
        super(Employee, self).__init__(name)
        ## Assign the salary of the employee
        self.salary = salary
        
## Create fish class
class Fish(object):
    pass

## Create Salmon class by extending Fish class
class Salmon(Fish):
    pass

## Create Halibut class by extending Fish class
class Halibut(Fish):
    pass

## using class to create objects
## rover is a Dog
rover = Dog("Rover")

# satan is a Cat
satan = Cat("Satan")

#Mary is a person
mary = Person("Mary")
## assign Satan as Mary's per
mary.pet = satan

# Frank is person who is an employee with $ 120000 salary
frank = Employee('Frank', 120000)
# rover is Frank's pet
frank.pet = rover

# Flipper is a fish create Flipper from Fish class
flipper = Fish()

## crouse is Salmon, create crouse from Salmon class
crouse = Salmon()

## harry is halibut, create harry from halibut class
harry = Halibut()



