'''
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return thrice of their sum.
'''

def numSum(num):
    num = map(int, num.split())
    if num[0] == num[1] and num[0] == num[2]:
        return sum(num) * 3
    else:
        return sum(num)

print numSum(raw_input("Enter three numbers separated by space: "))