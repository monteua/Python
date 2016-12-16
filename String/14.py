'''
Write a Python program that accepts a comma separated sequence of words as input and prints the unique
words in sorted form (alphanumerically)
'''

def unique_set(inp):

    inp = set(inp.lstrip().split(", "))

    return inp

print ", ".join(sorted(unique_set(raw_input('Enter the comma separated sequence of words: '))))