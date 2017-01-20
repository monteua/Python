'''
 Write a Python program to multiply all the items in a dictionary.
'''

dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
print ("Old dictionary:", dict1)
for key, value in dict1.items():
    dict1[key] = value * 10

print ("New dictionary:", dict1)