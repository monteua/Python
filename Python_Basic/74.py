'''
Write a Python program to input a number, if it is not a number generate an error message
'''

user_input = raw_input("Enter a number: ")

try:
    user_input = int(user_input)
    print user_input
except ValueError:
    print "Error! Not a number!"