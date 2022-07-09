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
