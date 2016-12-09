'''
Write a Python program to get numbers divisible by fifteen from a list using an anonymous function
'''

lst = [25, 15, 35, 45, 55, 75, 16, 365, 225]
print "Numbers divisible by fifteen are", list(filter(lambda x: (x % 15 == 0), lst))