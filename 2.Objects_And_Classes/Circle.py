'''The code below defines the Circle class. The class name is preceded by the keyword class
and followed by a colon ( : ). The initializer is always named _ _init_ _ , which is a
special method. Note that init needs to be preceded and followed by two underscores.
A data field radius is created in the initializer (line 6). The methods getPerimeter and
getArea are defined to return the perimeter and area of a circle (lines 8–12). More details
on the initializer, data fields, and methods will be explained in the following sections.'''

import math

class Circle:
    #construct a circle object
    def __init__(self, radius = 1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius
    

'''An object’s member refers to its data fields and methods. Data fields are also called instance
variables, because each object (instance) has a specific value for a data field. Methods are
also called instance methods, because a method is invoked by an object (instance) to perform
actions on the object such as changing the values in data fields for the object. In order to
access an object’s data fields and invoke an object’s methods, you need to assign the object to
a variable by using the following syntax:
instance methods
objectRefVar = ClassName(arguments)
For example,
c1 = Circle(5)
c2 = Circle()
You can access the object’s data fields and invoke its methods by using the dot operator ( . ),
also known as the object member access operator. The syntax for using the dot operator is:
dot operator (.)
objectRefVar.datafield
objectRefVar.method(args)'''

c = Circle(5)
print(c.radius)
print('The perimeter of the circle of radius 5cm is', c.getPerimeter())
print('The area of the circle of radius 5cm is', c.getArea())