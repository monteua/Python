'''
Write a Python program to sort a dictionary by key.
'''
from collections import OrderedDict

dict1 = {'zero': 0, 'one': 1, 'two': 2, 'three': 3}

print (dict(OrderedDict(sorted(dict1.items()))))