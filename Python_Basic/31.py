'''
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
'''

def commonDivisor(num1, num2):
    div = 1

    if num1 % num2 == 0:
        div = num2

    for i in range(num2/2, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            div = i
            break
    return div

if __name__ == '__main__':
    while True:
        print commonDivisor(int(raw_input("First number: ")), int(raw_input("Second number: ")))