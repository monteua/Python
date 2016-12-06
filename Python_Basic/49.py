'''
Write a Python program to calculate the hypotenuse of right angled triangle.
'''

import math

a = int(raw_input("enter a side: "))
b = int(raw_input("Enter the b side: "))

print "Hypotenuse is", math.sqrt(a**2 + b**2)