'''
Write a Python program to get file creation and modification date/times.
'''
import os, time


fname = raw_input("File name: ")

print "Modification time:", time.ctime(os.path.getmtime(fname))
print "Creation time:", time.ctime(os.path.getctime(fname))
