numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
           10: "ten", 11: "eleven", 12: "twelve", 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
           17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
           20: "twenty", 30: "thirty"}
halfs = {15: "quarter", 30: "half"}


def timeInWords(h, m):
    if m <= 30:
        if m == 0:
            return numbers[h] + " o' clock"
        elif m == 1:
            return numbers[m] + " minute past " + numbers[h]
        elif m in numbers and m not in halfs:
            return numbers[m] + " minutes past " + numbers[h]
        elif m < 30 and m != 15:
            return numbers[int(str(m)[0] + "0")] + " " + numbers[int(str(m)[1])] + " minutes past " + numbers[h]
        elif m in halfs:
            return halfs[m] + " past " + numbers[h]

    elif m > 30:
        new_m = 60-m
        if h == 12:
            h = 1
        else:
            h += 1

        if new_m == 1:
            return numbers[new_m] + " minute to " + numbers[h]
        elif new_m in numbers and new_m not in halfs:
            return numbers[new_m] + " minutes to " + numbers[h]
        elif new_m in halfs:
            return halfs[new_m] + " to " + numbers[h]
        else:
            return numbers[int(str(new_m)[0] + "0")] + " " + numbers[int(str(new_m)[1])] + " minutes to " + numbers[h]


print(timeInWords(4, 36))
print(timeInWords(8, 15))