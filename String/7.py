'''
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string.
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'
'''

def change_string(user_input):

    nt = user_input.find("not")
    bd = user_input.find('poor')

    # if position of 'poor' is bigger than 'not'
    if bd > nt:
        user_input = user_input.replace(user_input[nt:(bd+4)], 'good')

    return user_input

print change_string(raw_input("Enter the string: "))
