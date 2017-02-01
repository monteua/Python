'''
Write a Python program to check the validity of password input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
'''
import re

password = input("Enter the password: ")
not_valid = True
while not_valid:
    if len(password) < 6 or len(password) > 16:
        break
    elif not re.search('[a-z]', password):
        break
    elif not re.search('[A-Z]', password):
        break
    elif not re.search('[0-9]', password):
        break
    elif not re.search('[$#@]', password):
        break
    else:
        print ('Valid password!')
        not_valid = False

# we also can write print statement every time in if-else statement, before the 'break'
if not_valid:
    print ('Invalid password!')
