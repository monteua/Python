'''
Self powers
Problem 48 
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

# 1 line solution
print(str(sum([i**i for i in range(1, 1001)]))[-10:])

# 4 line solution
""" number = 0

for i in range(1, 1001):
    number += i**i
print(str(number)[-10:]) """