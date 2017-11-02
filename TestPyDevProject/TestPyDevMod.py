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

'''
# np array with zeros
np_azero = np.zeros((3,4))
print(type(np_azero))
print(np_azero)
print(np_azero.size)
print(np_azero.shape)
print(np_azero.dtype)
'''
'''
#np array with ones
np_aones = np.ones((2,3,4), dtype = np.int64)
print(type(np_aones))
print(np_aones)
print(np_aones.size)
print(np_aones.shape)
print(np_aones.dtype)
'''   
'''
# np empty array
np_aempty = np.empty((2,3,4), dtype = np.int64)
print(type(np_aempty))
print(np_aempty)
print(np_aempty.size)
print(np_aempty.shape)
print(np_aempty.dtype)
'''
'''
np_array = np.random.random((6,4))
#print(type(np_array))
#print(np_array)
#print(np_array.size)
#print(np_array.shape)
#print(np_array.dtype)
#print(np_array.sum())
#print(np_array.min())
#print(np_array.max())
#print(np_array.mean())
#print(np_array[2,3])
#print(np_array[:,1])
#print(np_array[1:3,:])
#print(np_array[1,2:4])
#print(np_array[1:4,1:4])

for row in np_array:
    print(row)

for element in np_array.flat: 
    print(element)
print(np_array.ravel())
print("")
print("----------")
print("")
print(np_array.reshape(12,2))
print("")
print("----------")
print("")
print(np_array.T)
print("")
print("----------")
print("")
print(np_array.T.shape)
print("")
print("----------")
print("")
'''

import matplotlib.pyplot as plt
def mandelbrot( h,w, maxit=20 ):
     """Returns an image of the Mandelbrot fractal of size (h,w)."""
     y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
     c = x+y*1j
     z = c
     divtime = maxit + np.zeros(z.shape, dtype=int)

     for i in range(maxit):
         z = z**2 + c
         diverge = z*np.conj(z) > 2**2            # who is diverging
         div_now = diverge & (divtime==maxit)  # who is diverging now
         divtime[div_now] = i                  # note when
         z[diverge] = 2                        # avoid diverging too much

     return divtime
 
plt.imshow(mandelbrot(400,400))
plt.show()