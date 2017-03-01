'''
Write a Python program to assess if a file is closed or not.
'''

fhand = open('file2.txt')

print (fhand.closed)
fhand.close()
print (fhand.closed)