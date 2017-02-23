'''
Write a Python program to read an entire text file.
'''

fhand = open('text.txt', 'r')

print (fhand.read())

fhand.close()