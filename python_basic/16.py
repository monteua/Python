'''
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
'''

number = int(raw_input("Enter the number: "))
if int(number) > 17:
    print (number - 17) * 2
else:
    print number - 17


