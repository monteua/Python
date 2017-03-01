'''
Write a Python program to remove newline characters from a file.
'''

with open('text.txt') as old:
    old = old.readlines()
    new = []
    for i in old:
        i = i.rstrip('\n')
        new.append(i)
    print (new)
