'''
Write a Python program to multiplies all the items in a list
'''

def multiply(lst):
    num = 1
    for i in lst:
        num *= i
    return num

print multiply([1, -5, 25, -6])
