'''
Write a Python program to get the maximum and minimum value in a dictionary.
'''

dict1 = {'zero': 0, 'one': 1, 'two': 2, 'three': 3}

mx = []
mn = []
for key, value in dict1.items():
    if value == max(dict1.values()):
        mx.append(str(key))
        mx.append(str(value))
    elif value == min(dict1.values()):
        mn.append(str(key))
        mn.append(str(value))

print ("Maximum item:", str.join(":", mx))
print ("Maximum key:", mx[0])
print ("Maximum value:", mx[1], '\n')
print ("Minimuum item:", str.join(":", mn))
print ("Minimuum key:", mn[0])
print ("Minimuum value:", mn[1])