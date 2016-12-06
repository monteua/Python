'''
Write a Python program to hash a word
'''

import hashlib

print hashlib.sha224(raw_input('Enter the word to be hashed (sha224): ')).hexdigest()