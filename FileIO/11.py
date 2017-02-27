'''
Write a Python program to write a list to a file.
'''

fhand = open('file2.txt', 'w')
fhand.truncate()
lst = [1, 2, 3, 'Green', 'Blue', 13]

for i in lst:
    fhand.write(str(i))
    fhand.write('\n')
fhand.close()

f = open('file2.txt', 'r')
f = f.read()
print (f)