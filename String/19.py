'''
Write a Python function to get the first half of a specified string of even length. Go to the editor
Sample function and result : string_first_half('Python') -> Pyt
'''

def string_first_half(inp):
    if len(inp) % 2 == 0:
        print inp[:len(inp)/2]

string_first_half('Python')