'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import sqrt

def get_sum(l):
    primes = list(range(l+1))
    primes[1] = 0
    for n in range(2, int(sqrt(l)) + 1):
        if primes[n] > 0:
            for i in range(n**2, l + 1, n):
                primes[i] = 0
    return sum(primes)

print (get_sum(10))
print (get_sum(2000000))