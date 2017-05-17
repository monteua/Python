'''
Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import sympy
import itertools

permutations = list(itertools.permutations('7654321'))
permutations = list(map(int, ["".join(i) for i in permutations]))

max_prime = 0

for p in permutations:
    if sympy.isprime(p) and p > max_prime:
        max_prime = p

print("Max:", max_prime)

