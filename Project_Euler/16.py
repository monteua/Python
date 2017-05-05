'''
Power digit sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def get_digits_sum(num):
    num = list(map(int, num.split("^")))
    power = str(num[0]**num[1])

    result = 0
    for i in power:
        result += int(i)
    return result

print (get_digits_sum('2^15'))
print (get_digits_sum('2^1000'))
