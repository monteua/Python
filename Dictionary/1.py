'''
Write a Python script to sort (ascending and descending) a dictionary by value
'''
import operator
dictionary = {3:40, 5:10, 0: 10, 1: 450, 2: 30}

print(sorted(dictionary.items(), key=operator.itemgetter(1)))