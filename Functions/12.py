'''
Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
'''

import string


def is_pangram(s):
    letters = list(string.ascii_lowercase)

    for letter in s:
        letter = letter.lower()
        if letter in letters:
            letters.remove(letter)
        else:
            continue
    if len(letters) == 0:
        return ("%s - is pangram" %s)
    else:
        return ("%s - is not pangram" %s)

print (is_pangram(input("Enter the string: ")))