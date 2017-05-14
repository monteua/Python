'''
Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial

factorials = [factorial(x) for x in range(10)]
result = 0

for i in range(10, factorial(9)*7):
    number = i
    total = 0

    while number > 0:
        total += factorials[number % 10]
        number //= 10

    if total == i:
        result += i
print(result)
