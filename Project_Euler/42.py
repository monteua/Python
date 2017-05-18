'''
Coded triangle numbers
Problem 42 
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we 
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle 
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common 
English words, how many are triangle words?
'''

from string import ascii_uppercase
from math import sqrt

letters_list = list(ascii_uppercase)

def is_triangle(num):
    d = sqrt((1-4*(-num*2)))
    x = (-1 + d) / 2
    if int(x) == x:
        return True


def get_sum(word):
    result = 0
    for letter in word:
        letter_pos = [pos for pos, value in enumerate(letters_list) if letters_list[pos] == letter]
        result += (letter_pos[0]+1)
    return is_triangle(result)


fhand = open('p042_words.txt', 'r')
fhand = fhand.read()
words_list = []

for word in fhand.split(","):
    words_list.append(word[1:-1])

count = 0

for word in words_list:
    if get_sum(word):
        count += 1
print("Triangle words in the file:", count)