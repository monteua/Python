'''
Write a Python program to filter the positive numbers from a list.
'''

lst = [4, -56, 2, -65, -2, 1, 6, 5]

new_lst = []
for i in lst:
    if i >=0:
        new_lst.append(i)
print new_lst
# sorted list
#print sorted(new_lst)