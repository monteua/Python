'''
Write a Python program to append text to a file and display the text.
'''

fhand = open('text.txt', 'a+')

text = "\nText to be added to the file."
fhand.writelines(text)

fhand.close()

