'''When passing a mutable object to a function, the function may change the contents of
the object.
Key
Point
Recall that numbers and strings are immutable objects in Python. Their contents cannot be
changed. When passing an immutable object to a function, the object will not be changed.
However, if you pass a mutable object to a function, the contents of the object may change.
The example in Listing 7.5 demonstrates the differences between an immutable object and
mutable object arguments in a function.'''



import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi
