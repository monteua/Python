'''
Write a Python program to convert degree to radian.
Note : The radian is the standard unit of angular measure, used in many areas of mathematics.
An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle;
one radian is just under 57.3 degrees (when the arc length is equal to the radius).
Test Data:
Degree : 15
Expected Result in radians: 0.2619047619047619
'''
import math

def to_radian(dg):
    return ("Radians: "+str(dg * (math.pi/180)))

print(to_radian(float(input("Degree: "))))