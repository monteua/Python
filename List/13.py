'''
Write a Python program to print the numbers of a specified list after removing even numbers from it.
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list()
for i in lst:
    if i % 2 != 0:
        new_list.append(i)

print (new_list)