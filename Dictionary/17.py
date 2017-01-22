'''
Write a Python program to remove duplicates from Dictionary.
'''

dict1 = {'name':
            {'name': 'Vadym',
                },
         'one': 1,
         'two': 2,
         'three': 3,
         'one':1,
         'zero':0
}
new_dict = {}
for key, value in dict1.items():
    if value not in new_dict.values():
        new_dict[key] = value
print (new_dict)
