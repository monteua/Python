#!/bin/python3
# https://www.hackerrank.com/challenges/electronics-shop/problem
import sys


def getMoneySpent(keyboards, drives, s):
    current_total = 0

    for keyboard in keyboards:
        for drive in drives:
            _sum = keyboard + drive
            if current_total > _sum <= s:
                current_total = _sum
    if current_total == 0:
        return -1
    return current_total

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
