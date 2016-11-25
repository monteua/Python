'''
Write a Python program to sum of two given integers. However if the sum is between 15 to 20 it will return 20.
'''

def sumInt(i1, i2):
    if 15 >= (i1 + i2) <= 20:
        return 20
    else:
        return i1 + i2





if __name__ == '__main__':
    while True:
        print sumInt(int(raw_input("First number: ")), int(raw_input("Second number: ")))