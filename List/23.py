'''
Write a Python program to find the second largest number in a list
'''

lst = [1, 4, 3, 5, 6, 9]

lst.remove(max(lst))
print (max(lst))