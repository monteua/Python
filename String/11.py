'''
Write a Python program to remove the characters which have odd index values of a given string.
'''

def remove_odd(inp):
    new_string = ""
    for i in range(0, len(inp)):
        if i % 2 == 0:
            new_string += inp[i]
    return new_string

print remove_odd(raw_input('Enter the string: '))