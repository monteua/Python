'''
Write a Python program to get the size of a file
'''

import os

fhand = raw_input("Enter the name of the file: ")

print "Size of the file:", os.path.getsize(fhand), 'bytes.'