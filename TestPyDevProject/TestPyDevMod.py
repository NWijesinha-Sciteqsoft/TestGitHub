import sys


'''
Created on Oct 14, 2017

@author: noel.wijesinha
'''
from array import array
from builtins import str
import numpy as np

if __name__ == '__main__':
    pass

# name = input("May I know your name? ")
# print("It"+"'"+"s a pleasure to meet you " + name +"!")
# age = input("Your age, please? ")
# print("So, you"+"'"+"re " + age + " years old, " + name + "!")
'''
matrix = [[1,2,3,4],
          [11,12,13,14],
          [21,22,23,24]]

np_matrix = np.array(matrix)
print(type(matrix))
'''

'''
for i in range(0,3):
    for j in range(0,4):
        
        print(matrix[i][j])
 '''
'''
# populate a np_a with 3 rows and 5 columns with 0-14   
np_a = np.arange(15).reshape(3,5)

#print np_a 
print(np_a)

#print shape of np_a
print(np_a.shape)

#print the number of axes (dimensions) of the np_a
print(np_a.ndim)

#print the total number of elements of the np_a
print(np_a.size)

#print the object describing type of the np_a
print(np_a.dtype)    

#print the tyoe of the np_a
print(type(np_a))

#print the size in bytes of each element of the np_a
print(np_a.itemsize)

#print the bufeer containing the actual elements of the np_a
print(np_a.data)
'''
'''       
#python arrays and print the types of the arrays
c = [1,2,3]
d = [1.2,1.4,1.6,2.1]
#print python array type of c
print(type(c))

#print python array type of d
print(type(d))

# asisgn to numpy arrays
np_c = np.array(c); np_d = np.array(d)

#print type of numpy arrays
print(np_c.dtype); print(np_d.dtype)
'''
'''
# create two dim numpy array
e = [1,2,3,4]; f = [5,6,7,8]
np_ef = np.array([e,f])
print(type(np_ef))
print(np_ef)
print(np_ef.size)
print(np_ef.shape)
print(np_ef.dtype)
'''



    