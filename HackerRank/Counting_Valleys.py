#!/bin/python3
#https://www.hackerrank.com/challenges/counting-valleys/problem
import sys

def countingValleys(n, s):
    current_lvl = 0
    valleys = 0

    for letter in s:
        if letter == "U":
            current_lvl += 1
        elif letter == "D":
            current_lvl -= 1
        if current_lvl == 0 and letter == "U":
            valleys += 1
    return valleys

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
