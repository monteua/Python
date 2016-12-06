'''
Write a Python program to get an absolute file path.
'''

import os

def getPath(fname):
    return os.path.abspath(fname)
file = raw_input("Enter the file name:")
print "Absolute file path is: ", getPath(file)
