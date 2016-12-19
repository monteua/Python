'''
Write a Python function to get a string made of its first three characters of a specified string.
If the length of the string is less than 3 then return the original string.
Sample function and result : first_three('ipy') -> ipy first_three('python') -> pyt
'''

def first_three(inp):
    if len(inp) <= 3:
        print inp
    else:
        print inp[:3]


first_three('ipy')
first_three('python')