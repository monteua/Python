'''
Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers
between 1 and 30 (both included)
'''

lst = list()
new_list = list()

for i in range(1,31):
    lst.append(i**2)

for n in lst[:5]:
    new_list.append(n)

for num in lst[-5:]:
    new_list.append(num)

print (new_list)