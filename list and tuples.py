# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L

['Michael Jackson', 10.2, 'pop', 10] #output

-----------------------------------------------------------------

# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L

['Michael Jackson', 10.2, ['pop', 10]] #output

-----------------------------------------------------------------

# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])

# Use append to add elements to list

L.append(['a','b'])
L

['Michael Jackson', 10.2, 'pop', 10, ['a', 'b']] #output 

-----------------------------------------------------------------

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

Before change: ['disco', 10, 1.2] #OUTPUT 
After change: ['hard rock', 10, 1.2]

-----------------------------------------------------------------

# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)

Before change: ['hard rock', 10, 1.2] #output 
After change: [10, 1.2]

-----------------------------------------------------------------

# Clone (clone by value) the list A

A = ["hard rock", 10, 1.2]
B = A
A[0] = "banana"
B = A[:]
B

['banana', 10, 1.2] #OUTPUT


#Now if you change A, B will not change

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

B[0]: banana #output 
B[0]: banana

-----------------------------------------------------------------

Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:

A = [1,'a']
B = [2,1,'d']
A+B

[1, 'a', 2, 1, 'd'] #output

