'''
Write a Python program to add two objects if both objects are integer type.
'''

while True:
    obj1 = raw_input("Object 1: ")
    obj2 = raw_input("Object 2: ")

    try:
        print int(obj1) + int(obj2)
    except ValueError:
        print "Not a number!"