'''
Write a Python function to create and print a list where the values are square of numbers between 1 and 30
(both included).
'''

def get_squares():
    lst = []

    for i in range(1, 31):
        lst.append(i*i)

    return lst

print (get_squares())
