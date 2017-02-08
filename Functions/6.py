'''
Write a Python function to check whether a number is in a given range.
'''

def check_range(num):
    if int(num) in range(0,11):
        print ("%s is in range from 0 to 10" % num)
    else:
        print ("%s is outside of the range from 0 to 10" % num)


check_range(input("Enter the number: "))