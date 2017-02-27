'''
Write a Python program to get the file size of a plain file.
'''

import os

fhand_size = os.stat('text.txt')

print ("File size in bytes is:", fhand_size.st_size)