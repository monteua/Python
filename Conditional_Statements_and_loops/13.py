'''
Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even
number. The numbers obtained should be printed in a comma-separated sequence
'''

numbers = list(range(100,401))
even_digits = list()
for i in numbers:
    count = 0
    for j in str(i):
        if int(j) % 2 == 0:
            count +=1
    if len(str(i)) == count:
        even_digits.append(str(i))
print (", ".join(even_digits))