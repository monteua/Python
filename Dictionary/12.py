'''
Write a Python program to remove a key from a dictionary.
'''

def remove_key(dict1):
    dict1.pop('removing')
    return dict1



print (remove_key({1: 1, 2: 4, 3: 9, 4: 16, 'removing':'this', 5: 25, 6: 36, 7: 49}))