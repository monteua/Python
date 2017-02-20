'''Write a Python program to calculate the sum of a list of numbers.'''

def get_sum(lst):
    return (sum(map(int, lst)))

print (get_sum([4, 5, 5, '1']))