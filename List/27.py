'''
Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number
'''

number = 100

not_prime = []
prime_list = []
for i in range(2, number+1):
    if i not in not_prime:
        prime_list.append(i)
    for j in range(i*i, number+1, i):
        not_prime.append(j)

print (prime_list)

