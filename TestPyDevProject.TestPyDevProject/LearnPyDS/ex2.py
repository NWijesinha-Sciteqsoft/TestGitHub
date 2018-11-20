'''
Created on Nov 20, 2018

@author: nwijesinha

This exercise to introduce Array and using arrays in Python
List: It is similar to array with the exception that the data elements can be of different data types. 
You can have both numeric and string data in a Python list.

'''

# Define list for the exercise
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1,2,3,4,5]
list3 = ['a', 'b', 'c','d']

# Accessing values in a list to print all elements
print("Printing List 1 elements")
for i in range(len(list1)):
    print("list1[%i]" % i, list1[i])

print("Printing List 2 elements")
for j in range(len(list2)):
    print("list2[%i]" % j,list2[j])

print("Printing List 3 elements")
for k in range(len(list3)):
    print("list3[%i]" % k,list3[k])
    
# Accessing values in a list using concatinating another list
# Update list 
list2 = list2 + [6,7]
print("Printing List 2 elements")
for j in range(len(list2)):
    print("list2[%i]" % j,list2[j])

# print the list element based on index range
print("List2[1:5]", list2[1:5])

# Updating the list by giving the slice on the left
list5 = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2: ")
print(list5[2])
# Update index 2 with 2001
list5[2] = 2001
print("New value available at index 2: ")
print(list5[2])

# Deleting elements in a list
print("Printing List 5")
print(list5)
print("List length: ", len(list5))
del list5[2]
print("After deleting value at index 2: ")
print(list5)
print("List length: ", len(list5))




 


