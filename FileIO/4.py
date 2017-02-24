'''
Write a Python program to read last n lines of a file.
'''

fhand = ((open('text.txt', 'r')).read()).split("\n")

for element in fhand:
    if len(element) < 1:
        fhand.remove(element)

inp = input("Enter the number of lines: ")

print ("\n".join(fhand[-int(inp):]))