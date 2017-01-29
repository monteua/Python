'''
Write a Python program to remove an item from a set if it is present in the set.
'''

s = {0, 1, 2, 3, 4, 5}

item_to_remove = 3

if item_to_remove in s:
    s.remove(item_to_remove)
print (s)