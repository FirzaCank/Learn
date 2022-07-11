#TABLE OF CONTENT
1. Mean and STD
2. Max and Min
3. Addition
4. Subtraction
5. Multiplication
6. Divison
7. Dot Product
8. Adding constant to a numpy array
9. Math function - PI AND SIN
10. Linspace - easier array maker
11. Iterating 1-D Arrays

#NUMPY STATISTICAL FUNCTION MEAN AND STD

a = np.array([1, -1, 1, -1])
mean = a.mean()
mean

#OUTPUT
0

standard_deviation=a.std()
standard_deviation

#output
1

-------------------------------------------------------
#NUMPY STATISTICAL FUNCTION MAX AND MIN

b = np.array([-1, 2, 3, 4, 5])
max_b = b.max()
min_b = b.min()
max_b
min_b

#output
5
-1

-------------------------------------------------------
#NUMPY ARRAY OPERATIONS (+)

u = np.array([1, 0])
v = np.array([0, 1])

# NUMPY ARRAY ADDITION (+)
z = np.add(u, v)
z

#output
array([1, 1])

-------------------------------------------------------
# Plotting functions - Garis vektor
import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
%matplotlib inline  

def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
 
-------------------------------------------------------
#ARRAY SUBSTRACTION

a = np.array([10, 20, 30])
b = np.array([5, 10, 15])
c = np.subtract(a, b)
print(c)

#OUTPUT
[ 5 10 15]

-------------------------------------------------------
#ARRAY MULTIPLICATION

x = np.array([1, 2])
y = np.array([2, 1])
z = np.multiply(x, y)
z

#output
array([2, 2])

-------------------------------------------------------
#ARRAY DIVISION

a = np.array([10, 20, 30])
b = np.array([2, 10, 5])
c = np.divide(a, b)
c

#OUTPUT
array([5.,2.,6.])

-------------------------------------------------------
#DOT PRODUCT

X = np.array([1, 2])
Y = np.array([3, 2])
np.dot(X, Y)

#OUTPUT
7 --------- # (1.3)+(2.2)

-------------------------------------------------------
#ADDING CONSTANT TO A NUMPY ARRAY

u = np.array([1, 2, 3, -1])
u + 1

#OUTPUT
array([2,3,4,0])

-------------------------------------------------------
#MATHEMATICAL FUNCTION - PI AND SIN

# The value of pi
np.pi

#output
3.141592653589793



# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements
y = np.sin(x)
y

#output
array([0.0000000e+00, 1.0000000e+00, 1.2246468e-16])

-------------------------------------------------------
#LINSPACE
#A useful function for plotting mathematical functions is linspace. Linspace returns evenly spaced numbers over a specified interval.

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)

#output
array([-2., -1.,  0.,  1.,  2.])



# Make a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)

#output
array([-2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ])



# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
plt.plot(x, y)

-------------------------------------------------------
#Iterating 1-D Arrays

arr1 = np.array([1, 2, 3])
print(arr1)

#output
[1 2 3]

for x in arr1:
  print(x)
  
#output
1
2
3
