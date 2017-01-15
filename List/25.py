'''
Write a Python program to get the frequency of the elements in a list
'''

import collections

lst = [1, 4, 3, 5, 6, 9, 1, 5, 6]

print (dict(collections.Counter(lst)))