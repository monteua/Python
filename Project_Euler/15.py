'''
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

from math import factorial


def get_paths(grid_size):
    f = factorial(grid_size)
    return factorial(grid_size * 2) / f ** 2

print("Number of routes:", int(get_paths(2)))
print("Number of routes:", int(get_paths(20)))
