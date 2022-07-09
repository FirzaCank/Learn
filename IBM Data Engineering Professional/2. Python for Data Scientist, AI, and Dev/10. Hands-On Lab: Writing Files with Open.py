# We can open a file object using the method write() to save the text file to a list.
# To write to a file, the mode argument must be set to w. Let’s write a file Example2.txt with the line: “This is line A”

# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
   
# We can read the file to see if it worked    
# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

#output
This is line A
    
----------------------------------------------------------------------------------------------------------------------------  
# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Read file
with open(exmp2, 'r') as readfile:
  print(readfile.read())
  
#output
This is line A
This is line B

----------------------------------------------------------------------------------------------------------------------------
# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

# Write the strings in the list to text file
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
        
#output
This is line A

This is line B

This is line C



# Verify if writing to file is successfully executed
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
#output
This is line A
This is line B
This is line C

----------------------------------------------------------------------------------------------------------------------------
# However, note that setting the mode to w overwrites all the existing data in the file.

with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

#output
Overwrite

----------------------------------------------------------------------------------------------------------------------------
#Appending Files 'a'


Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open(exmp2,'w') as writefile:
  for line in Lines:
    print(line)
    writefile.write(line)
    
with open(exmp2,'a') as writefile:
  writefile.write('This is line C\n')
  writefile.write('This is line D\n')
  writefile.write('This is line E\n')

  RUN
  
with open(exmp2, 'r') as readfile:
  print(readfile.read())
  
#OUTPUT
This is line A
This is line B
This is line C
This is line C
This is line D
This is line E

----------------------------------------------------------------------------------------------------------------------------
