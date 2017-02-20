'''
Write a Python program to get the sum of a non-negative integer.
Test Data :
sumDigits(345) -> 12
sumDigits(45) -> 9
'''

def sumDigits(number):
    s = 0
    if number > 0:
        for i in str(number):
            s += int(i)
    return s

print (sumDigits(76))