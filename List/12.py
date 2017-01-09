'''
Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'Black']
'''

def remove_elements(lst):
    pos = [0, 2, 4, 5]
    new_list = list()

    for i in range(len(lst)):
        if i in pos:
            continue
        else:
            new_list.append(lst[i])

    return new_list

print (remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))