'''
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''

def intSum(i1, i2, i3):
    if i1 == i2 or i1 == i3 or i2 == i3:
        return 0
    else:
        return i1 + i2 + i3

if __name__ == '__main__':
    while True:
        print intSum(int(raw_input("First number: ")), int(raw_input("Second number: ")), \
                     int(raw_input("Third number: ")))