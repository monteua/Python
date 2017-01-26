'''
Write a Python program to find the repeated items of a tuple
'''

t = (4, 5, 4, 8, 25, 16, 8)

d = dict()

for item in t:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1

for key, value in d.items():
    if value > 1:
        print (key)