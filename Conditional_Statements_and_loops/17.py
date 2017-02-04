'''
Write a Python program to check a triangle is valid or not.
Input the length of side1: 5
Input the length of side2: 4
Input the length of side3: 6
The triangle is valid.
'''

side1 = int(input("Input the length of side1: "))
side2 = int(input("Input the length of side2: "))
side3 = int(input("Input the length of side3: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print ("The triangle is valid.")
else:
    print ("The triangle is invalid.")



