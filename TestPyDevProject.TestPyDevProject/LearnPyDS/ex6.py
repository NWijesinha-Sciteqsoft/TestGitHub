'''
Created on Nov 22, 2018

@author: nwijesinha

This exercise is to lean use of Matrix array in Python
Matrix:
Matrix is a special case of two dimensional array where each data element is of strictly same size.
Every matrix is also a two dimensional array but not vice versa. 
Matrices are very important data structures for many mathematical and scientific calculations. 

'''
# Import numpy for matrix
from numpy import *

# Array to capture temprature for a week
a = array([["Mon", 18, 20, 22, 17],
           ["Tue", 11, 18, 21, 18],
           ["Wed", 15, 21, 20, 19],
           ["Thu", 11, 20, 22, 21],
           ["Fri", 18, 17, 23, 22],
           ["Sat", 12, 22, 20, 18],
           ["Sun", 13, 15, 19, 16]])
# Define a 7x5 matrix array using reshape metho available in numpy
m = reshape(a, (7, 5))
# Print length of the matrix array
print("Printing the length of the matrix array")
print(len(m))
print("*"*20)  # print * 20 times
# Print the matrix array
print("Printing the matrix array")
print(m)
print("*"*20)  # print * 20 times
# Print the matrix array using a loop
print("Printing the matrix array using for loop")
for i in m:
    for j in i:
        print(j, " ")
    print()
print("*"*20)  # print * 20 times
# Another way of print matrix array by looping
print("Another way of printing the matrix array using for loop")
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j])
    print()
print("*"*20)  # print * 20 times
# Print elements in matrix array by providing row 
print("Print elements in matrix array by providing row")
print(m[2])
print("*"*20)
# Print elements in matrix array by providing row and column
print("Print elements in matrix array by providing row and column")
print(m[4][3])
print("*"*20)

'''
Adding a row to the end of the matrix array, 
remember the row has to contain same size array 
as the current arrays in the matrix
'''
# creating a new matrix by adding a row to the end by using append function and assigning it to the new matrix
m_r = append(m, [['Avg', 12, 15, 13, 11]], 0)
print("Printing the matrix array")
print(m_r)
print("*"*20)  # print * 20 times

'''
Adding a column to the end of the matrix array, 
remember the column has to contain same number of rows 
'''
# creating a new matrix by adding a column to the end by using insert function and assigning it to the new matrix
m_c = insert(m, [5], [[10], [20], [22], [20], [18], [17], [17]], 1)
print("Printing the matrix array")
print(m_c)
print("*"*20)  # print * 20 times

# Deleting a row from matrix
# Assign m matrix to m1
m1 = m
print("Printing matrix before deleting a row")
print(m1)
print("*" * 20)

print("Deleting row in index 2")
# Delete row 2 using delete function and reassign the matrix to m1 by specifying index of the row and axis value of 0 for row
m1 = delete(m1, [2], 0)
# print matrix after deleting
print("Printing matrix after deleting a row")
print(m1)
print("*" * 20)

# Deleting a column from matrix
# Assign matrix m to m2
m2 = m
# Print matrix before deleting column
print("Printing matrix before deleting column")
print(m2)
print("*" * 20)
# Delete the column using delete function by specifying the index of the column and axis value 1 for column
print("Deleting column in index 2")
m2 = delete(m2, s_[2], 1)
# Print matrix after deleting column
print("Printing matrix after deleting column")
print(m2)
print("*" * 20)

# Updating a row in a matrix
# Assign m matrix to m3
m3 = m 
print("Printing the matrix before update")
print(m3)
print("*" * 20)
# Updating the matrix row for Thursday with index of 3
print("Updating values for Thursday to '0'")
m3[3] = ['Thu', 0, 0 , 0, 0]
print("Print the matrix after update")
print(m3)
print("*" * 20)
