'''
Prime permutations
Problem 49 
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) 
each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is 
one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from itertools import permutations, combinations_with_replacement
import sympy

permutation = set(["".join(i) for i in list(combinations_with_replacement('012345678901234567892699', 4))])
prime_list = [int(i) for i in permutation if sympy.isprime(i) and int(i) > 999]

for i in prime_list:
    for p in prime_list:
        q = p + abs(i-p)
        if q in prime_list:
            if i != p and p != q and i != q:
                perm = ["".join(k) for k in list(permutations(str(p), 4))]
                if str(i) in perm and str(p) in perm and str(q) in perm:
                    print("Sequence:", i, p, q)
                    print("Number:", str(i) + str(p) + str(q))