'''
Write a Python program to test whether a number is within 100 or 1000 or 2000
'''

def testNumber(num):
    if num <= 100:
        return "Number is lower than 100"
    elif num <= 1000:
        return "Number is within 101 and 1000"
    elif num <= 2000:
        return "Number is within 1001 and 2000"
    else:
        return "Number is greater than 2000"


print testNumber(int(raw_input("Enter the number: ")))