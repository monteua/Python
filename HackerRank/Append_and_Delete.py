#!/bin/python3

import sys

def appendAndDelete(s, t, k):
    string = None
    for string in range(k, 0, -1):
        if len(s) == 0 or s == t[:len(s)] and len(t) - len(s) == string:
            break
        s = s[:-1]
    if len(t) - len(s) <= string:
        return "Yes"

    else:
        return "No"


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
