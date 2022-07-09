# create object Circle

import matplotlib.pyplot as plt
%matplotlib inline

class Circle(object):

  #constructor
  def __init__(self,radius = 3, color ='red'):
    self.radius = radius
    self.color = color

  #method
  def add_radius(self, r):
    self.radius = self.radius + r
    return(self.radius)

  # Method
  def drawCircle(self):
    plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
    plt.axis('scaled')
    plt.show()
    
---------------------------------------------------------------------------------------
# Create an object RedCircle
RedCircle = Circle(10, 'red')

# Find out the methods can be used on the object RedCircle
dir(RedCircle)
#output
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'add_radius',
 'color',
 'radius']

---------------------------------------------------------------------------------------
# Print the object attribute radius and color

print(RedCircle.radius)
print(RedCircle.color)

#output
10
red

---------------------------------------------------------------------------------------
# Set the object attribute radius

RedCircle.radius = 1
RedCircle.radius

#output
1

---------------------------------------------------------------------------------------
#Use method to change the object attribute radius - ini yang udah diubah radiusnya jadi 1

print('Radius of object:',RedCircle.radius)

RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)

RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

#output
Radius of object: 1
Radius of object of after applying the method add_radius(2): 3
Radius of object of after applying the method add_radius(5): 8

---------------------------------------------------------------------------------------
# Create a blue circle with a given radius - polymorphisme

BlueCircle = Circle(radius=100)
print(BlueCircle.radius)
print(BlueCircle.color)

#output
100
red

---------------------------------------------------------------------------------------
#Final Task
class analysedText(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

---------------------------------------------------------------------------------------
#Check whether each def is passed or failed 
import sys

sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )
    
