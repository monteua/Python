'''
Write a Python function that checks whether a passed word is palindrome or not.
'''

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

if is_palindrome(input("Enter a word: ")) == True:
    print ("Word is palindrome")
else:
    print ("Word is not palindrome")