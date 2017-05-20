'''
Permuted multiples
Problem 52 
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different 
order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''


x = 1

while True:
    d = set(str(x))
    if all(set(str(p * x)) == d for p in range(2, 7)):
        print("Smallest positive integer is:", x)
        break
    x += 1

