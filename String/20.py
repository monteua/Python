'''
Write a Python function to reverses a string if it's length is a multiple of 4.
'''

def is_multiple(inp):
    if len(inp) % 4 == 0:
        print inp[::-1]

is_multiple("Pythonnn")