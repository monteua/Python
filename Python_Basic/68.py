'''
Write a Python program to swap two variables
'''

a = raw_input("A: ")
b = raw_input("B: ")

print "Before swaping\nA:" , a, "B:", b

a, b = b, a
print "After swaping\nA:" , a, "B:", b