'''
Write a Python program to check if a given positive integer is a power of two.
'''

def is_power_of_two(num):
    return (num > 0 and (num & (num - 1) == 0))

print (is_power_of_two(55))
print (is_power_of_two(16))
print (is_power_of_two(35))
