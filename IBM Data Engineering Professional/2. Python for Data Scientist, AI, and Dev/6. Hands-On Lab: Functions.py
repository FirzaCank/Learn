# First function example: Add 1 to a and store as b

def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)
 


# Get a help on add function

help(add)



Help on function add in module __main__: #output

add(a)
    add 1 to a

-------------------------------------------------------------
# Function Definition

def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

# Initializes Global variable  

x = 3
# Makes function call and return function a y
y = square(x)
y

3 if your square + 1 10 #output
10

--------------------------------------------------------------------------------------------------------------------------
# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

MJ()
Michael Jackson #output

MJ1()
Michael Jacksonv #output

# See what functions returns are

print(MJ())
print(MJ1())

Michael Jackson #output
None
Michael Jackson
None

--------------------------------------------------------------------------------------------------------------------------
# Define the function for combining strings

def con(a, b):
    return(a + b)

# Test on the con() function

con("This ", "is")
This is #output

--------------------------------------------------------------------------------------------------------------------------
# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1   

5 #output



# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2   

0 #output


# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c)

print(equation(5,5))  5 #output
print(equation(0,0))  0 #output

--------------------------------------------------------------------------------------------------------------------------
# way to create global variables from within a function as follows:

artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

Michael Jackson is an artist #output
Whitney Houston is an artist #output

--------------------------------------------------------------------------------------------------------------------------
# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# AC/DC's rating is: 10.0       #output
# Deep Purple's rating is: 0.0
# My favourite band is: AC/DC

--------------------------------------------------------------------------------------------------------------------------
# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable 

del myFavouriteBand

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)

# AC/DC's rating is:  10.0        #output
# Deep Purple's rating is:  0.0
# name 'myFavouriteBand' is not defined

--------------------------------------------------------------------------------------------------------------------------
#Collections and Functions

def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
        
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

No of arguments: 3 #output
Horsefeather
Adonis
Bone
No of arguments: 4
Sidecar
Long Island
Mudslide
Carriage

--------------------------------------------------------------------------------------------------------------------------
#Dictionary Arguments, The arguments can also be packed into a dictionary as shown:

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

Country : Canada            #output
Province : Ontario
City : Toronto

--------------------------------------------------------------------------------------------------------------------------
#They can accept (and return) data types, objects and even other functions as arguements. Consider the example below:

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)


['One', 'Two', 'Three', 'Four'] #output


myList
