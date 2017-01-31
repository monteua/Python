'''
Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as
output (all characters in lower case).
'''

lines = []

while True:
    user = input("Enter a line: ")
    if user:
        lines.append(user.lower())
    else:
        break
for i in lines:
    print (i)