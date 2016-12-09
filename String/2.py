'''
Write a Python program to count the number of characters (character frequency) in a string
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

chr = dict()

user_input = raw_input("Enter the string: ")

for i in user_input:
    if i in chr:
        chr[i] += 1
    else:
        chr[i] = 1
print chr