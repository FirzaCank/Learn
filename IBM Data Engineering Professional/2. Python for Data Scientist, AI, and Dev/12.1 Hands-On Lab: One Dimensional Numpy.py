#TABLE OF CONTENT :
1. Check type value
2. Assign value
3. Slicing
4. Assign value with list
5. Other attributes (size, dim, shape)


#NumPy is a Python library used for working with arrays, linear algebra, fourier transform, and matrices.A numpy array is similar to a list.
#NumPy stands for Numerical Python and it is an open source project
#The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Create a python list
a = ["0", 1, "two", "3", 4]
# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

#output
a[0]: 0
a[1]: 1
a[2]: two
a[3]: 3
a[4]: 4

--------------------------------------------------------------------------------------------------------------------------------------------------
#NUMPY ARRAY SAME TYPE

import numpy as np

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a

#output
array([0, 1, 2, 3, 4])



# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

#output
a[0]: 0
a[1]: 1
a[2]: 2
a[3]: 3
a[4]: 4

  
  
# Check the type of the array
type(a)

#output
numpy.ndarray



# Check the type of the values stored in numpy array
a.dtype

#output
dtype('int32')

--------------------------------------------------------------------------------------------------------------------------------------------------
#ASSIGN VALUE

# Create numpy array
c = np.array([20, 1, 2, 3, 4])

# Assign the first element to 100 and 5th element to 0
c[0] = 100
c[4] = 0
c

#output
array([100,   1,   2,   3,   0])

--------------------------------------------------------------------------------------------------------------------------------------------------
#SLICING

# Slicing the numpy array
d = c[1:4]
d

#output
array([1,2,3])



#We can assign the corresponding indexes to new values as follows:
# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c

#output
array([100,1,2,300,400])



#We can also define the steps in slicing, like this: [start:end:step].
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

#output
[2 4]



#If we don't pass start its considered 0
print(arr[:4])

#output
[1 2 3 4]



#If we don't pass end it considers till the length of array.
print(arr[4:])

#output
[5 6 7]



#If we don't pass step its considered 1
print(arr[1:5:])

#output
[2 3 4 5]



#Test
#Print the even elements in the given array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1::2])

#output
[2 4 6 8]

--------------------------------------------------------------------------------------------------------------------------------------------------
#ASSIGN VALUE WITH LIST

c
#output
array([100,   1,   2, 300, 400])

# Create the index list
select = [0, 2, 3, 4] ------> ini adalah index yang akan dipilih di array c
# Use List to select elements
d = c[select]
d

#output
array([100,   2, 300, 400])



# Assign the specified elements to new value
c[select] = 100000
c

#output
array([100000,      1, 100000, 100000, 100000])

--------------------------------------------------------------------------------------------------------------------------------------------------
#OTHER ATTRIBUTES

a = np.array([0, 1, 2, 3, 4])

# Get the size of numpy array
a.size

#output
5



#The attribute ndim represents the number of array dimensions, or the rank of the array. In this case, one:
# Get the number of dimensions of numpy array
a.ndim

#output
1



#The attribute shape is a tuple of integers indicating the size of the array in each dimension:
# Get the shape/size of numpy array
a.shape

#output
(5,)
