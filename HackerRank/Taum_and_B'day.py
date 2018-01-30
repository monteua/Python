#!/bin/python3


def taumBday(b, w, x, y, z):

    result = 0

    if x <= y+z:
        result += b*x
    if y <= x+z:
        result += w*y
    if x > y+z:
        result += b*(y+z)
    if y > x+z:
        result += w*(x+z)
    return result

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        b, w = input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = taumBday(b, w, x, y, z)
        print(result)
