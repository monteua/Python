'''
Write a Python program that will accept the base and height of a triangle and compute the area.
'''

def computeArea(height, base):
    print "Area is", 0.5 * base * height

if __name__ == '__main__':

    while True:
        computeArea(int(raw_input("Enter the height of the triangle: ")), \
                          int(raw_input("Enter the base of the triangle: ")))