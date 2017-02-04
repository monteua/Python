'''
Write a Python program to check a string represent an integer or not.
Input a string: Python
The string is not an integer.
'''

inp = input("Input a string: ")

try:
    inp = int(inp)
    print ("The string is an integer!")
except:
    print ("The string is not an integer.")