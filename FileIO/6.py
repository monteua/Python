'''
Write a Python program to read a file line by line store it into a variable.
'''
file = (open('text.txt', 'r')).readlines()
content = ""

for i in file:
    content += i

print(content)