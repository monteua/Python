'''
Write a Python program to find  the greatest common divisor (gcd) of two integers.
'''

def get_gcd(a, b):
    min_number = min([a,b])
    gcd_so_far = None
    for i in range(1, min_number+1):
        if a % i == 0 and b % i == 0:
            gcd_so_far = i
    return gcd_so_far

print (get_gcd(26,39))