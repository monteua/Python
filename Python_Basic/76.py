'''
Write a Python program to compute the product of a list of integers (without using for loop)
'''

lst = [30, 10, 45, 60]

print reduce(lambda x, y: x *y, lst)
