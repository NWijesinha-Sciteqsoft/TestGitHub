'''
Created on Oct 15, 2017

@author: noel.wijesinha
@title: Employee Class
@description: This class will create employee attributes to be manipulated and print on the screen
'''
from pydoc import classname
from random import *
from test.test_codeccallbacks import NoEndUnicodeDecodeError


class EmployeeClass(object):
    '''
    classdocs
    '''

    def __init__(self, first_name, last_name, street_address_1, street_address_2, city, state, zip_code, country, home_phone, mobile, ssn):
        '''
        Constructor
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.street_address_1 = street_address_1
        self.street_address_2 = street_address_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.home_phone = home_phone
        self.mobile = mobile
        self.ssn = ssn
        self.username = first_name + "." + last_name
        self.email = self.username + "@companyname.com"
        self.emp_number = str(randint(1, 100))
        
    def PrintEmpName(self):
        return self.first_name + " " + self.last_name
    
    def Print_EmpInfo(self):
        return "Employee Name: " + self.PrintEmpName() + " " + "Employee Number: " + self.emp_number + " " + "Employee SSN: " + self.ssn
      
    def Clear_EmpInfo(self):
        self.first_name = ""
        self.last_name = ""
        self.street_address_1 = ""
        self.street_address_2 = ""
        self.city = ""
        self.state = ""
        self.zip_code = ""
        self.country = ""
        self.home_phone = ""
        self.mobile = ""
        self.ssn = ""
        self.username = ""
        self.email = ""
        self.emp_number = ""

    
