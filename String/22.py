'''
Write a Python program to sort a string lexicographically
'''

def lex_sorting(inp):

    return sorted(sorted(inp), key=str.upper)

print lex_sorting('Python2.7')
print lex_sorting('silver-elite')