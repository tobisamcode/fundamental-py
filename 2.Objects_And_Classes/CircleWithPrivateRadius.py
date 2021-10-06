'''Hiding Data Field
To prevent direct modifications of data fields, don’t let the client directly access data fields.
This is known as data hiding. This can be done by defining private data fields. In Python, the
private data fields are defined with two leading underscores. You can also define a private
method named with two leading underscores.
Private data fields and methods can be accessed within a class, but they cannot be accessed
outside the class. To make a data field accessible for the client, provide a get method to return
its value. To enable a data field to be modified, provide a set method to set a new value.
Colloquially, a get method is referred to as a getter (or accessor), and a set method is
referred to as a setter (or mutator).
A get method has the following header:
'''

import math
class Circle:
    def __init__ (self, radius = 1):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    
def main():
    c = Circle(5)
    print('the radius is', c.getRadius())

main()