'''
Write a Python program to reverse words in a string.
'''
import collections

string = 'Write a Python program to reverse words in a string.'
new_string = collections.deque()
for i in string.split():
    new_string.appendleft(i)
    
print " ".join(new_string)