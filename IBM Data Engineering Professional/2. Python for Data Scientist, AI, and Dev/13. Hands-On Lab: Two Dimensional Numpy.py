#Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
A
A.ndim
A.shape
A.size

#output
array([[11, 12, 13],
       [21, 22, 23],
       [31, 32, 33]])
2
(3,3)
9

-----------------------------------------------
#Accessing different elements of a Numpy Array

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)

# Access the element on the second row and third column
A[1, 2]
A[1][2]
A[0][0]
A[0][0:2] #Access the element on the first row and first and second columns
A[0:2, 2] #Access the element on the first and second rows and third column

#output
23
23
11
array([11,12])
array([13, 23])

-----------------------------------------------
#BASIC OPERATION

X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]]) 
Z = X + Y
Z

#output
array([[3, 1],
       [1, 3]])



Y = np.array([[2, 1], [1, 2]]) 
Z = 2 * Y
Z

#output
array([[4, 2],
       [2, 4]])


#MATRIX MULTIPLICATION
Y = np.array([[2, 1], [1, 2]]) 
X = np.array([[1, 0], [0, 1]]) 
Z = X * Y
Z

#output
array([[2, 0],
       [0, 2]])


#FUNCITION DOT
A = np.array([[0, 1, 1], [1, 0, 1]])
A
#output
array([[0, 1, 1],
       [1, 0, 1]])

B = np.array([[1, 1], [1, 1], [-1, 1]])
B
#output
array([[ 1,  1],
       [ 1,  1],
       [-1,  1]])

Z = np.dot(A,B)
Z
#output
array([[0, 2],
       [0, 2]])

-----------------------------------------------------------
#TRANSPOSED MATRIX

C = np.array([[1,1],[2,2],[3,3]])
C
#output
array([[1, 1],
       [2, 2],
       [3, 3]])

C.T
#output
array([[1, 2, 3],
       [1, 2, 3]])

-----------------------------------------------------------
#QUIZ 2D NUMPY ARRAY

#convert it to Numpy Array.
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
a = np.array(a)
a
#output
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])


#Access the element on the first row and first and second columns.
a[0][0:2]
#output
array([1, 2])
