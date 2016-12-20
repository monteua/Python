'''
Write a Python function to convert a given string to
all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
'''

def to_upper(inp):
    count = 0

    for i in inp[:4]:
        if i.upper() == i:
            count += 1
    if count > 1:
        return inp.upper()
    return inp


print to_upper('PythOn')
print to_upper('PYThon')