'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def getPrime(num):
    largest = []
    a, b = num, 2
    while a > 1:
        if a % b == 0:
            largest.append(b)
            a = a/b
        else:
            b += 1
    print (max(largest))
getPrime(13195)
getPrime(600851475143)