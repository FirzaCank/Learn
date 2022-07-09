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
#Additional modes
#It's fairly ineffecient to open the file in a or w and then reopening it in r to read any lines. Luckily we can access the file in the following modes:

# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists.
# You dont have to dwell on the specifics of each mode for this lab.

# Let's try out the a+ mode:
with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )
    
#output
Initial Location: 115
Read nothing

New Location : 0
Overwrite
This is line C
This is line D
This is line E
This is line C
This is line D
This is line E
This is line E

Location after read: 115

    
    
# In the following code block, Run the code as it is first and then run it with the .truncate().
with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())
 
#output
Line 1
Line 2
Line 3
finished
is line D
This is line E
This is line C
This is line D
This is line E
This is line E

----------------------------------------------------------------------------------------------------------------------------
# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
                
# Verify if the copy is successfully executed
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())
    
#output
Line 1
Line 2
Line 3
finished
is line D
This is line E
This is line C
This is line D
This is line E
This is line E
----------------------------------------------------------------------------------------------------------------------------
#EXERCISE
#Your local university's Raptors fan club maintains a register of its active members on a .txt document.
#Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
#Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file.
#Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )



#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)

            ----------

def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            header = members[0]
            members.pop(0)
                
            inactive = [member for member in members if ('no' in member)]
            '''
            The above is the same as 

            for member in members:
            if 'no' in member:
                inactive.append(member)
            '''
            #go to the beginning of the write file
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()
                
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)

# code to help you see the files

headers = "Membership No  Date Joined  Active  \n"

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
    
#output
Active Members: 


Membership No  Date Joined  Active  
    15424      2018-11-10   yes   
    55264      2018-8-1     yes   
    36773      2019-1-8     yes   
    41013      2017-10-17   yes   
    30730      2019-3-23    yes   
    43516      2018-1-10    yes   
    43387      2017-11-10   yes   
    89001      2016-8-10    yes   
    56757      2018-8-4     yes   
    98523      2017-10-24   yes   
    31042      2020-12-7    yes   

Inactive Members: 


Membership No  Date Joined  Active  
    10329      2015-8-13    no    
    27031      2018-6-18    no    
    36193      2020-7-6     no    
    52812      2019-9-13    no    
    66490      2017-6-23    no    
    75244      2016-2-6     no    
    18316      2020-4-15    no    
    29308      2015-12-23   no    
    74988      2019-6-13    no    
    23802      2020-7-13    no    
    77202      2015-1-8     no    
    22632      2020-4-5     no 
