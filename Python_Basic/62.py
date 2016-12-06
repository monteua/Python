'''
Write a Python program to test if a certain number is greater than all numbers of a list.
'''

user_input = raw_input("Enter the number: ")
lst = [1, 25, 562, 356, 123]
greater = False

for i in lst:
    if int(user_input) > i:
        greater = True
    else:
        greater = False

if greater == True:
    print "Your number is greater than any number of the list", lst
else:
    print "Your number is not greater than any number of the list", lst