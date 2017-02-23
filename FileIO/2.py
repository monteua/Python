'''
Write a Python program to read first n lines of a file.
'''

fhand = (((open("text.txt", 'r')).read()).split('\n'))

user_input = input("Enter the number of lines: ")
count = 0
for line in fhand:
    if count < int(user_input):
        print (line)
        count += 1
    else:
        break
