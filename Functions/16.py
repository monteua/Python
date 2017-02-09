'''
Write a Python program to access a function inside a function.
'''

def add_one(num):
    def add_two(num2):
        nonlocal num
        return num + num2

    return add_two

first = add_one(5)
print (first(10))