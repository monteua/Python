'''
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def getLargestPalindrome(num_of_digits):
    palindromes = []
    minimum = int("1" + (num_of_digits-1)*"0")
    #print (minimum)
    maximum = int("1" + (num_of_digits)*"0")
    #print (maximum)
    numbers = range(minimum, maximum+1)

    for i in numbers:
        for p in numbers:
            result = i * p
            reversed_result = str(result)[::-1]
            if int(result) == int(reversed_result):
                palindromes.append(result)
    print (max(palindromes))

getLargestPalindrome(3)