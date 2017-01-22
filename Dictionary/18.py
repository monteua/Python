'''Write a Python program to check a dictionary is empty or not.'''

not_empty = {'name':
             {'name': 'Vadym',
              },
         'one': 1,
         'two': 2,
         'three': 3,
         'one': 1,
         'zero': 0
         }
empty = {}

if len(not_empty) >= 1:
    print ("Dictionary #1 is not empty!")
else:
    print("Dictionary #1 is empty!")

if len(empty) >= 1:
    print ("Dictionary #2 is not empty!")
else:
    print("Dictionary #2 is empty!")