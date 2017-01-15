'''
Write a Python program to count the number of elements in a list within a specified range
'''

import collections

# input data
elements_range = [4, 8]
lst = [1, 4, 3, 5, 6, 9, 1, 5, 6]

# new list within specified range
new_list = []

# find all elements, which satisfy the range of elements
for i in lst:
    if i >= elements_range[0] and i <= elements_range[1]:
        new_list.append(i)

# count the number of elements in a new list
print (dict(collections.Counter(new_list)))