'''
Write a Python program to change a given string to a new string where the first and last chars have been exchanged
'''

def swap_letters(inp):

    return inp[-1].capitalize()+inp[1:len(inp)-1]+inp[0].lower()

print swap_letters(raw_input("Enter the string: "))