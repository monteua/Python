'''
Write a Python program to create a Caesar encryption.
Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each
letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a
left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar,
who used it in his private correspondence.
'''

import string

letters_upper = list(string.ascii_uppercase)
letters_lower = list(string.ascii_lowercase)


#encrypt
def encrypt():

    user_input = raw_input("Enter the string to be encrypted: ").split(" ")
    number_of_shifts = int(raw_input("Enter the number of shifts:"))
    encrypted = list()

    for word in user_input:
        encrypted_word = ""
        for letter in word:

            #letter is in upper case
            if letter in letters_upper:
                pos = letters_upper.index(letter)
                crypting = (pos + number_of_shifts) % 26
                encrypted_word += letters_upper[crypting]

            # letter is in lower case
            elif letter in letters_lower:
                pos = letters_lower.index(letter)
                crypting = (pos + number_of_shifts) % 26
                encrypted_word += letters_lower[crypting]
        encrypted.append(encrypted_word)

    print " ".join(encrypted)

#decrypt

def decrypt():
    user_input = raw_input("Enter the string to be decrypted: ").split(" ")
    number_of_shifts = int(raw_input("Enter the number of shifts:"))
    decrypted = list()

    for word in user_input:
        decrypted_word = ""
        for letter in word:

            if letter in letters_upper:
                pos = letters_upper.index(letter)
                decrypting = (pos - number_of_shifts) % 26
                decrypted_word += letters_upper[decrypting]

            elif letter in letters_lower:
                pos = letters_lower.index(letter)
                decrypting = (pos - number_of_shifts) % 26
                decrypted_word += letters_lower[decrypting]
        decrypted.append(decrypted_word)

    print " ".join(decrypted)

start = raw_input("Encrypt or decrypt? [E or D]:")

if start.lower().startswith("e"):
    encrypt()
elif start.lower().startswith('d'):
    decrypt()
