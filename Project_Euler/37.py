'''
Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379,
37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

# 7 sec solution
import sympy
import time

start = time.time()
primes = []
current_prime = 11

while len(primes) < 11:

    i = str(current_prime)

    if all(sympy.isprime(int(i[:num + 1])) and sympy.isprime(int(i[num:])) for num in range(len(str(i)))):
        primes.append(int(i))
    current_prime = sympy.nextprime(current_prime)

print("Prime's list:", primes)
print("Sum:", sum(primes))
print("Elapsed Time:", time.time()-start)



# 10 sec solution
'''
import sympy
import time

start = time.time()
# generate primes in range from 8 to 1 000 000
def get_primes():
    x = list(sympy.primerange(8, 1000000))
    return x

trunc = []
primes = get_primes()
for i in primes:
    i = str(i)

    if all(sympy.isprime(int(i[:num + 1])) and sympy.isprime(int(i[num:])) for num in range(len(str(i)))):
        trunc.append(int(i))
print("Prime's list:", trunc)
print("Sum:", sum(trunc))
print("Elapsed Time:", time.time()-start)
'''


