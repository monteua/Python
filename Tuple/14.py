'''
Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
'''
lst1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

lst1[2] = lst1[2][:2] + (100,)

print (lst1)