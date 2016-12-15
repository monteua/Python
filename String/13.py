'''
Write a Python script that takes input from the user and displays that input back in upper and lower cases.

'''

def convert_string(inp):
    print inp.capitalize()
    print inp.lower()

convert_string(raw_input("Enter the string: "))