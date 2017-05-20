'''
Consecutive prime sum
Problem 50 
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import sympy


def get_sum(limit):
    primes = list(sympy.primerange(1, limit))
    prime_sum = [0]
    for p in primes:
        prime_sum.append(prime_sum[-1] + p)
        if prime_sum[-1] >= limit:
            break

    terms = 1
    for i in range(len(prime_sum)):
        for j in range(len(prime_sum) - 1, i + terms, -1):
            n = abs(prime_sum[i] - prime_sum[j])
            if j - i > terms and sympy.isprime(n):
                terms = j - i
                max_prime = n
                break

    return "Max prime with limit " + str(limit) + " is " + str(max_prime) + " with " + str(terms) + " terms."

print(get_sum(100))
print(get_sum(1000))
print(get_sum(1000000))
