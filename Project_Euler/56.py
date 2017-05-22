'''
Powerful digit sum
Problem 56 
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: 
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''


def get_digits_sum(a, b):
    number = str(a ** b)
    # convert the number to a digit list
    digits_list = [int(i) for i in number]
    # return the sum of the digits to the caller
    return sum(digits_list)

result = 0

for a in range(1, 100):
    for b in range(1, 100):
        digital_sum = get_digits_sum(a, b)
        # searching for the maximum digital sum from the given range from 0 to 100
        if digital_sum > result:
            result = digital_sum
print("Maximum digital sum is:", result)
