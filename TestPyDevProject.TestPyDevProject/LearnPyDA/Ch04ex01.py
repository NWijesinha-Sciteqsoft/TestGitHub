'''
Created on Jan 14, 2019

@author: nwijesinha

Learn about the Numpy ndarry which is multidimensional array object in Python Numpy

'''

import numpy as np

# Create a array called data1
data1 = [6, 7.5, 8, 0, 1]
# Create an ndarray array1 using numpy and assign data1 array values
array1 = np.array(data1)
# Print raay1
print(array1)
# print shape of array 1
print(np.shape(array1))
print(np.ndim(array1))
print(array1.dtype)

# Create an array called data2
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
array2 = np.array(data2)
print(array2)
print(np.shape(array2))
print(np.ndim(array2))
print(array2.dtype)

# create an array of zero
array3 = np.zeros(10)
print(array3)
print(np.shape(array3))
print(np.ndim(array3))
print(array3.dtype)

# create an array with initializing the elements
array4 = np.empty((3, 6))
print(array4)
print(np.shape(array4))
print(np.ndim(array4))
print(array4.dtype)

# create an array with using arange which is array valued version of Python built in range function
array5 = np.arange(15, dtype=np.float64)
print(array5)
print(np.shape(array5))
print(np.ndim(array5))
print(array5.dtype)

# converting array type
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
int64_arr = arr.astype(np.int64)
print(int64_arr.dtype)
float_arr = int64_arr.astype(np.float64)
print(float_arr.dtype)

# converting an array from float to interger
arr1 = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr1)
print(arr1.dtype)
print(arr1.astype(np.int32))
print(arr1, arr1.dtype)

# converting array of string to number
numeric_string = np.array(['1.24', '-9.36', '42'], dtype=np.string_)
print(numeric_string, numeric_string.dtype)
print(numeric_string.astype(float))

in_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50])
in_array.astype(calibers.dtype)
print(in_array)

empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)

# Arithmetic operators Numpy arrays
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2 * arr2)
print(arr2 - arr2)
print(1 / arr2)
print(arr2 ** 0.5)

# basic indexing and slicing on Numpy arrays
arr3 = np.arange(10)
print(arr3)
print(arr3[5])
print(arr3[5:8])
arr3[5:8] = 12
print(arr3)
# array slice are view and any updated to the array slice will be reflected on the source array
arr_slice = arr3[5:8]
arr_slice[1] = 12345
print(arr3)
arr_slice[:] = 64
print(arr3)
# copying an array with out creating avice
arr_copy = arr3[5:8].copy()
print(arr3)
print(arr_copy)
arr_copy[:] = 100
print(arr3)
print(arr_copy)

# Higher dimension arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
# two ways of accessing an element in a higher dimension array
print(arr2d[0][2])
print(arr2[0, 2])

# Multidimensional array example using Numpy
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
# assigning scalar values and arrays
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)
print(arr3d[1, 0])

# Indexing with slices
arr = np.arange(10)
print(arr[1:6])
print(arr2d);
print(arr2d[:2]); 
print(arr2d[:2, 1:])

# Boolean indexing in Python using Numpy
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print("Printing names array")
print(names)
print("Printing data array")
print(data)
# compare 'Bob' to elements in array names
print(names == 'Bob')
# passing a boolean array to index an array
print(data[names == 'Bob'])
# mixing a boolean arrays with slices
print(data[names == 'Bob', 2:])
print(data[names == 'Bob', 2:])
print(data[names == 'Bob', 3])
print(names != 'Bob')
mask = (names == 'Bob') | (names == 'Will')
print(mask)
print(data[mask])

