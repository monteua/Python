'''
Write a Python program to calculate the area of a trapezoid.
Note : A trapezoid is a quadrilateral with two sides parallel. The trapezoid is equivalent to the British definition of
the trapezium. An isosceles trapezoid is a trapezoid in which the base angles are equal so.
Test Data:
Height : 5
Base, first value : 5
Base, second value : 6
Expected Output: Area is : 27.5
'''

def get_area(height, base1, base2):
    return ("Area is: " + str(((base1 + base2) / 2) * height))

print (get_area(float(input("Height: ")), float(input("Base, first value: ")), float(input("Base, second value: "))))