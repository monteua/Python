'''
Write a Python program to find the highest 3 values in a dictionary.
'''

dict1 = {8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
max_3 = list()
for i in range(3):
    max_3.append(max(dict1.values()))
    dict1.pop(max(dict1))

print ("Hightest 3 values is:", ", ".join(map(str,max_3)))

