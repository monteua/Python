'''
Write a Python program to check whether an alphabet is a vowel or consonant.
'''

letter = input("Enter the letter: ")

if letter in ['a', 'e', 'i', 'o', 'u']:
    print (letter, 'is vowel')
else:
    print (letter, 'is consonant')
