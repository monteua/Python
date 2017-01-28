'''
Write a Python program to count the elements in a list until an element is a tuple.
'''

t = [4, 5, 4, 8, 25, 16, (70, 80, 90), 'python', 8]

count = 0

for i in t:
    if isinstance(i, tuple):
        break
    count += 1
print (count)