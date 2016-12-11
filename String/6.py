'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

user_input = raw_input('Enter the string: ')

if len(user_input) < 3:
    print user_input
elif user_input[len(user_input)-3:] == 'ing':
    print user_input + 'ly'
else:
    print user_input + 'ing'