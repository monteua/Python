'''
Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a
rectangle.
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def compute_area(self):
        return ("Area is: " + str(self.length * self.width))

rect = Rectangle(10, 15)
print (rect.compute_area())