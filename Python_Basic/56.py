'''
Write a Python program to calculate the sum of the digits in an integer.
'''

user_input = raw_input("enter the number:")

sum = 0

for i in user_input:
    sum += int(i)

print sum