'''
Write a Python program to calculate surface volume and area of a cylinder.
Test Data:
volume : Height (4), Radius(6)
Expected Output:
Volume is : 452.57142857142856
Surface Area is : 377.1428571428571
'''

import math

def get_volume(height, radius):
    return ("Volume is: " + str(math.pi * radius ** 2 * height))
def get_surface_area(height, radius):
    return ("Surface Area is: " + str((2 * math.pi * radius * height) + (math.pi * radius ** 2) * 2))

height = float(input("Enter height: "))
radius = float(input("Enter the radius: "))

print (get_volume(height, radius))
print (get_surface_area(height, radius))