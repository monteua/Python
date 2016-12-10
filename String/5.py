'''
Write a Python program to get a single string from two given strings, separated by a space and swap the first
two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''

str1 = raw_input("enter the two strings separated by a space: ").split()
print (str1[1][:2]+str1[0][2:]), (str1[0][:2]+str1[1][2:])
