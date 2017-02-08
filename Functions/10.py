'''
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
'''

def is_even(lst):
    even = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            continue
    return even

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print ("Given list:", sample)
print ("Even numbers:", is_even(sample))