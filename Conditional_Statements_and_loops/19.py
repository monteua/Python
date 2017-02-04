'''
Write a Python program to check a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.

Expected Output:

Input lengths of the triangle sides:
x: 6
y: 8
z: 12
Scalene triangle
'''

side1 = int(input("Input the length of side1: "))
side2 = int(input("Input the length of side2: "))
side3 = int(input("Input the length of side3: "))

if side1 == side2 and side2 == side3:
    print ("Equilateral triangle")
elif side1 != side2 and side2 != side3:
    print ("Scalene triangle")
else:
    print ("Isosceles triangle")