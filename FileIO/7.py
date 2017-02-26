'''
Write a python program to find the longest word.
'''

file = (open('text.txt', 'r')).read()

largest_so_far = ''

for p in file.split("\n"):
    for i in p.split(" "):
        if len(i) > len(largest_so_far):
            largest_so_far = i
print (largest_so_far)
