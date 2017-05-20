'''
Combinatoric selections
Problem 53 
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''

from math import factorial


def combinations(n):
    # short solution
    return sum([1 for r in range(n+1) if (factorial(n) / (factorial(r)*(factorial((n-r))))) > 1000000])

print("Result:", sum([combinations(n) for n in range(101)]))

# easy to read solution
'''
def combinations(n):
    count_combinations = 0
    for r in range(n+1):
        if (factorial(n) / (factorial(r)*(factorial((n-r))))) > 1000000:
            count_combinations += 1
    return count_combinations


count = 0
for n in range(101):
    result = combinations(n)
    count += result
print("Result:", count)
'''