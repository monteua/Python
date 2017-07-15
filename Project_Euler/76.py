'''
Counting summations
Problem 76 
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''


def get_ways(target_num):
    return [1] + [0]*target_num


def get_numbers(target_num):
    return range(1, target_num)

c = get_ways(100)
for i in get_numbers(100):
    for p in range(i, 101):
        c[p] += c[p-i]
print("Result:", c[-1])

