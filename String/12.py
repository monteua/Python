'''
Write a Python program to count the occurrences of each word in a given sentence.
'''

def count_word(inp):
    count = dict()

    inp = inp.split(" ")

    for i in inp:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

print count_word(raw_input("Enter the string: "))