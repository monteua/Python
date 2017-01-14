'''
Write a Python program to find the index of an item in a specified list.
'''

list1 = [1, 4, 3, 5, 6, 9]
def find_index(item, lst):
    for index, value in enumerate(lst):
        if value == item:
            return (index)





print (find_index(6, list1))