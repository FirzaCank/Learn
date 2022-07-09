# Create your first tuple

tuple1 = ("disco",10,1.2 )
type(tuple1)

tuple #output 

-----------------------------------------------------------
# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

disco #output
10
1.2

-----------------------------------------------------------
# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

<class 'str'> #output
<class 'int'>
<class 'float'>

-----------------------------------------------------------
# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
tuple2

('disco', 10, 1.2, 'hard rock', 10) #output

-----------------------------------------------------------
# Sort the tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)
RatingsSorted

[0, 2, 5, 6, 6, 8, 9, 9, 10] #output

-----------------------------------------------------------
# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

Element 0 of Tuple:  1
Element 1 of Tuple:  2
Element 2 of Tuple:  ('pop', 'rock')
Element 3 of Tuple:  (3, 4)
Element 4 of Tuple:  ('disco', (1, 2))

-----------------------------------------------------------
# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

Element 2, 0 of Tuple:  pop
Element 2, 1 of Tuple:  rock
Element 3, 0 of Tuple:  3
Element 3, 1 of Tuple:  4
Element 4, 0 of Tuple:  disco
Element 4, 1 of Tuple:  (1,2)

-----------------------------------------------------------
# Print the first and second element in the second nested tuples

NestedT[2][1][0]
NestedT[2][1][1]

r #output
o

-----------------------------------------------------------
# Print the first and second element in the second nested tuples

NestedT[4][1][0]
NestedT[4][1][1]

1
2
