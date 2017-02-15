'''
Write a Python class named Circle constructed by a radius and two methods which will compute the area and the
perimeter of a circle.
'''
import math

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return ("Area of the circle is: " + str(round(math.pi * self.r**2, 3)))
    def perimeter(self):
        return ('Perimeter of the circle is: ' + str(round(2*self.r*math.pi, 3)))

newcircle = Circle(10)
print (newcircle.area())
print (newcircle.perimeter())

