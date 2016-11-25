'''
Write a Python program to compute the future value of a specified principal amount,
rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
'''

amt = 10000
int = 3.5
years = 7

value = 10000

for i in range(years):
    value += value/100*3.5
print value