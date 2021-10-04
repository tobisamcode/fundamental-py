import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi



def main():
    # create a circle of radius 1
    Circle1 = Circle()
    print("The area of the circle of radius", Circle1.radius, 'is', Circle1.getArea())

    # create a circle of radius 25
    Circle2 = Circle(25)
    print('The area of the circle of radius', Circle2.radius, 'is', Circle2.getArea())

    # create a circle of radius 125
    circle3 = Circle(125)
    print('The area of the circle of radius', circle3.radius, 'is', circle3.getArea())

main()