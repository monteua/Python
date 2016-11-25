'''
Write a Python program to get the least common multiple (LCM) of two positive integers.
'''


def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while (True):
        if ((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1

    return lcm


if __name__ == '__main__':
    while True:
        print lcm(int(raw_input("First number: ")), int(raw_input("Second number: ")))
