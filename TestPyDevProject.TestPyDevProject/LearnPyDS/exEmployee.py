'''
Created on Dec 17, 2018

@author: nwijesinha

This example is to import a library and create a program

'''
from HumanResourcePkg.EmployeeClass import EmployeeClass

if __name__ == '__main__':
    # Define employee class emp_1
    emp_1 = EmployeeClass("noel", "wijesinha", "186 Ascalon Drive", "", "Maple", "ON", "L6A0M8", "Canada", "289-217-4288", "416-9856300", "463-345-123")
    # Print emplyee name
    print("Employee Name:" + emp_1.PrintEmpName()) 
    # Print employee information
    print(emp_1.Print_EmpInfo())
    # print size of the employee class emp_1
    print(emp_1.__sizeof__())
    # Clear employee information
    emp_1.Clear_EmpInfo()
    # Print employee name
    print("Employee Name:" + emp_1.PrintEmpName()) 
    # Print emplyee information
    print(emp_1.Print_EmpInfo())
    # Print size of emplyee class emp_1
    print(emp_1.__sizeof__())

