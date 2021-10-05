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


# print a tables of areas for radius
def printAreas(c, times):
        print("Radius \t\tAreas")
        while times >= 1:
            print(c.radius, "\t\t", c.getArea())
            c.radius = c.radius + 1
            times = times - 1 


def main():
    # Create a circle object with radius 1
    myCircle = Circle()

    # Print areas for radius 1, 2, 3, 4, and 5
    n = 5
    printAreas(myCircle, n)

    # Display myCircle.radius and times

    print("\nRadius is", myCircle.radius)
    print("n is", n)

main()