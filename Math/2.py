'''
Write a Python program to convert radian to degree.
Test Data:
Radian : .52
Expected Result : 29.781818181818185
'''
import math

def to_degree(rd):
    return ("Degrees: "+str(rd * 180/math.pi))

print(to_degree(float(input("Radians: "))))