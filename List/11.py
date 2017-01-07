'''
Write a Python function that takes two lists and returns True if they have at least one common member.
'''

lst1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
lst2 = ['Green', 'White', 'Black']
count = 0

for i in lst1:
    if i in lst2:
        count +=1

if count >=1:
    print ("Match found")
else:
    print ("No common members")