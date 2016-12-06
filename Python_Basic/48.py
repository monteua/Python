'''
Write a Python program to convert height (in feet and inches) to centimeters
'''

def convertLenght(height):
    height = height.split(" ")

    return int(height[0]) * 30.48 + int(height[2]) * 2.54


if __name__ == "__main__":
    height = raw_input("Enter the height (1 ft 5 in): ")

    print "Centimeters: ", convertLenght(height)
