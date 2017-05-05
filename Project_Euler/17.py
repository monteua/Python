'''
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''


def less20(num):
    # 13
    phrase = simple[num]
    return len(phrase)


def less100(num):
    # 65
    x, y = str(num)
    if int(y) > 0:
        phrase = teen[int(x)] + simple[int(y)]
    else:
        phrase = teen[int(x)]
    return len(phrase)


def less1000(num):
    x, y, z = str(num)
    # 845
    if int(y) > 1 and int(z) > 0:
        phrase = simple[int(x)] + 'hundred' + 'and' + teen[int(y)] + simple[int(z)]
    elif int(y) == 1 and int(z) > 0:
        phrase = simple[int(x)] + 'hundred' + 'and' + simple[int(y + z)]
    elif int(y) > 1 and int(z) == 0:
        phrase = simple[int(x)] + 'hundred' + 'and' + teen[int(y)]
    elif int(y) == 1 and int(z) == 0:
        phrase = simple[int(x)] + 'hundred' + 'and' + simple[int(y + z)]
    elif int(z) > 0 and int(y) == 0:
        phrase = simple[int(x)] + 'hundred' + 'and' + simple[int(z)]
    else:
        phrase = simple[int(x)] + 'hundred'
    return len(phrase)


def is1000():
    # 1000
    phrase = simple[1] + 'thousand'
    return len(phrase)


if __name__ == "__main__":
    simple = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
              10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
              17: "seventeen", 18: "eighteen", 19: "nineteen"}
    teen = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    r = 1000
    count = 0
    while r > 0:
        if r < 20:
            count += less20(r)
            r -= 1
        elif r < 100:
            count += less100(r)
            r -= 1
        elif r < 1000:
            count += less1000(r)
            r -= 1
        elif r == 1000:
            count += is1000()
            r -= 1
    print(count)
