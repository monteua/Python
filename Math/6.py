'''
Write a Python program to calculate surface volume and area of a sphere.
Note: A sphere is a perfectly round geometrical object in three-dimensional space that is the surface of a completely
round ball.
Test Data:
Radius of sphere : .75
Expected Output :
Surface Area is : 7.071428571428571
Volume is : 1.7678571428571428
'''

import math

def get_volume(radius):
    return ("Volume is: " + str(4/3*math.pi*radius**3))
def get_area(radius):
    return ("Surface Area is: " + str(4*math.pi*radius**2))

radius = float(input("Enter the radius: "))

print (get_area(radius))
print (get_volume(radius))

