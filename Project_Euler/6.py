'''
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_of_squares(num):
    numbers = range(1, num+1)
    result = 0
    for i in numbers:
        result += i*i
    return result
def square_of_sum(num):
    numbers = range(1, num + 1)
    return sum(numbers)**2

print (square_of_sum(10) - sum_of_squares(10))
print (square_of_sum(100) - sum_of_squares(100))