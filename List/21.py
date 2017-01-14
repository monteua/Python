'''
Write a Python program to select an item randomly from a list
'''

import random

list1 = random.sample(range(1,255), 10)
print("List:", list1)
print ("Random item from the list:", random.choice(list1))