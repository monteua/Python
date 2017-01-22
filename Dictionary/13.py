'''
 Write a Python program to map two lists into a dictionary
'''

list1 = ['zero', 'one', 'two', 'three']
list2 = [0, 1, 2, 3]

print (dict(zip(list1, list2)))