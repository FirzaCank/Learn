a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
        
(1) b = 1
# Please enter a number to divide a1      #output
# Success a= 1.0

(2) b = 0

# Please enter a number to divide a0      #output
# There was an error

----------------------------------------------------------------------------
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

(1) b = 1
# Please enter a number to divide a1      #output
# Success a= 1.0

(2) b = 0
# Please enter a number to divide a0      #output
# The number you provided cant divide 1 because it is 0

(3) b = a
# Please enter a number to divide aa      #output
# You did not provide a number

----------------------------------------------------------------------------
# With Finally

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
    
# Please enter a number to divide a1    #output
# success a= 1.0
# Processing Complete
