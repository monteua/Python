'''
Write a Python program which accept the user's first and
last name and print them in reverse order with a space between them.
'''

fname, lname = raw_input("First name: "), raw_input('Last name: ')
print fname[::-1], lname[::-1]