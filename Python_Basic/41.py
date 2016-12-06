'''
Write a Python program to check whether a file exists.
'''

fname = raw_input("Enter the file name: ")
try:
    open(fname, 'r')
    print "Found it!"
except IOError:
    print "File does not exist!"