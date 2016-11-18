'''
Write a Python program to accept a filename from the user print the extension of that.
Sample filename : abc.java
Output : java
'''

filename = raw_input("Enter the file name: ")
print filename.strip().split('.')[1]