'''
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''
import string

def check_string(inp):
    uppercase = 0
    lowercase = 0

    for letter in inp:
        if letter in string.ascii_uppercase:
            uppercase += 1
        elif letter in string.ascii_lowercase:
            lowercase += 1
        else:
            continue
    print ("No. of Upper case characters :", uppercase)
    print ("No. of Lower case Characters :", lowercase)

check_string(input("Enter the string to check: "))
