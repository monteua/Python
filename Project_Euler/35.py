'''
Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from math import sqrt


def get_primes(l):
    primes = list(range(l+1))
    primes[1] = 0
    for n in range(2, int(sqrt(l)) + 1):
        if primes[n] > 0:
            for i in range(n**2, l + 1, n):
                primes[i] = 0
    new_list = []
    for i in primes:
        if i != 0:
            new_list.append(i)

    return new_list

prime_list = get_primes(1000000)
count = 0

for i in prime_list:
    num = str(i)
    if all(int(num[p:] + num[:p]) in prime_list for p in range(len(num))):
        count += 1
    print (count)
print(count)

