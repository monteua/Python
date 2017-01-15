'''
Write a Python program to find the second smallest number in a list.
'''

lst = [1, 4, 3, 5, 6, 9]

lst.remove(min(lst))
print (min(lst))