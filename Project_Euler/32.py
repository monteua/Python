'''
Digit cancelling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
 believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

denom = 1
for i in range(1, 10):
    for p in range(1, i):
        x = divmod(9*p*i, 10*p-i)
        if not x[1] and x[0] <= 9:
            denom *= i / p

print(denom)

