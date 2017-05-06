'''
Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def factorial_number(factorial):
    result = 1
    for i in range(1, factorial+1):
        result *= i
    return ("Number is: " + str(result) + "\nSum of digits: " + str(sum([int(x) for x in str(result)])))

print(factorial_number(10))
print(factorial_number(100))
