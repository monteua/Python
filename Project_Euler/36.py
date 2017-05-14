'''
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
import time
start = time.time()


def is_palindrome(num):
    num = str(num)
    if int(num) == int(num[::-1]):
        return True
    return False


def get_sum(limit):
    result = 0
    for i in range(limit):
        if is_palindrome(i) and is_palindrome(int(bin(i)[2:])):
            result += i
    return result

print(get_sum(1000000))
print(time.time() - start)