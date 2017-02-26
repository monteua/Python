'''
Write a Python program to count the number of lines in a text file.
'''

file = (open('text.txt', 'r')).read()
file = file.split("\n")

print (len(file))