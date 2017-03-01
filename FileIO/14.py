'''
Write a Python program to read a random line from a file.
'''
import random

with open('text.txt', 'r') as file:
    file = file.readlines()
    print (random.choice(file))
    