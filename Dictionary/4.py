'''
Write a Python script to check if a given key already exists in a dictionary.
'''

dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def check_key(k):
    if k in dictionary:
        print ("Key is already in the dictionary.")
    else:
        print ("Key is not found in the dictionary.")

check_key(5)
check_key(7)