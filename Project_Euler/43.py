'''
Sub-string divisibility
Problem 43 
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import itertools
import time

start = time.time()
_sum = 0
digits = [(1, 4, 2), (2, 5, 3), (3, 6, 5), (4, 7, 7), (5, 8, 11), (6, 9, 13), (7, 10, 17)]

permutations = list(itertools.permutations('0123456789', 10))
permutations = ["".join(i) for i in permutations]

for number in permutations:
    if all(int(number[d[0]:d[1]]) % d[2] == 0 for d in digits):
        _sum += int(number)

print(_sum)
print("Time elapsed:", round((time.time() - start), 2))
