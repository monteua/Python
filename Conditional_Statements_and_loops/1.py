'''
Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
(both included).
'''

numbers = []
for i in range(1500, 2701, 1):
    if i % 7 == 0 and i % 5 == 0:
        numbers.append(str(i))
print (",".join(numbers))