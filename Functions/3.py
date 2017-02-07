'''
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''

def multiply(lst):
    mult = 1
    for i in lst:
        mult *= i
    return mult

print (multiply([8, 2, 3, -1, 7]))