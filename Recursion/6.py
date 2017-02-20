'''
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
Test Data :
sum_series(6) -> 12
sum_series(10) -> 30
'''

def sum_series(number):
    n = 0
    result = 0
    while n <= number:
        result += (number - n)
        n += 2
    return result

print (sum_series(6.25))
print (sum_series(6))
print (sum_series(10))