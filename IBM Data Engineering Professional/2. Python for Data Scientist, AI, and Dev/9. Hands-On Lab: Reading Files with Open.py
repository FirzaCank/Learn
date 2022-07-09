## Uncomment these if working locally, else let the following code cell run.

import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

##Download Example file
# !wget -O /resources/data/Example1.txt
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt

--------------------------------------------------------------------------------------------------------------------------------------------------------------
#Download Data

from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(filename, "Example1.txt")
--------------------------------------------------------------------------------------------------------------------------------------------------------------
#READING TEXT FILES

# One way to read or write a file in Python is to use the built-in open function.
# The open function provides a File object that contains the methods and attributes you need in order to read, save, and manipulate the file.
# In this notebook, we will only cover .txt files. The first parameter you need is the file path and the file name. An example is shown as follow:

file = open("/resource/data/Example1.txt","r")

#The mode argument is optional and the default value is r. In this notebook we only cover two modes:
# **r**: Read mode for reading files
# **w**: Write mode for writing files

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Read the Example1.txt
example1 = "Example1.txt"
file1 = open(example1, "r")



# Print the path of file
file1.name

#output
Example1.txt



# Print the mode of file, either 'r' or 'w'
file1.mode

#output
'r'

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Read the file
FileContent = file1.read()
FileContent

#output
'This is line 1 \nThis is line 2\nThis is line 3'



# Print the file with '\n' as a new line
print(FileContent)

#output
This is line 1 
This is line 2
This is line 3



# Type of file content
type(FileContent)

#output
str

--------------------------------------------------------------------------------------------------------------------------------------------------------------
#It is very important that the file is closed in the end. This frees up resources and ensures consistency across different python versions.
# Close file after finish

file1.close()

--------------------------------------------------------------------------------------------------------------------------------------------------------------
#A Better Way to Open a File
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/ReadWith.png

# Open file using with
example1 = "Example1.txt"
file1 = open(example1, "r")

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
    
    
    
# Verify if the file is closed
file1.closed

#output
True



# See the content of file
print(FileContent)

#output
This is line 1 
This is line 2
This is line 3

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))
    
#output
This

# Once the method .read(4) is called the first 4 characters are called. If we call the method again, the next 4 characters are called.
# The output for the following cell will demonstrate the process for different inputs to the method read():
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/read.png

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

#output
This
 is 
line 1 

This is line 2



# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

#output
This is line 1 

This 
is line 2

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# We can also read one line of the file at a time using the method readline():

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

#output
first line: This is line 1 
  
  
# We can also pass an argument to  readline()  to specify the number of charecters we want to read.
# However, unlike  read(),  readline() can only read one line at most.
with open(example1, "r") as file1:
    print(file1.readline(20))   # does not read past the end of line
    print(file1.read(20))       # Returns the next 20 chars

#output
This is line 1 

This is line 2
This 



# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
            
#output
Iteration 0 :  This is line 1 

Iteration 1 :  This is line 2

Iteration 2 :  This is line 3
  
--------------------------------------------------------------------------------------------------------------------------------------------------------------  
# We can use the method readlines() to save the text file to a list:

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()
  
  
  
# Print the first line
FileasList[0]

#output
'This is line 1 \n'
