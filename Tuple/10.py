'''
Write a Python program to remove an item from a tuple.
'''

#tuple are immutable. It means, that you cannot add, delete, or change elements within the tuple
# but there are other way

t = (4, 5, 4, 8, 25, 16, 'python', 8)
print ("Old tuple:", t)
# we want to remove the word from the tuple

t = t[:6] + t[7:]

print ("New tuple:", t)