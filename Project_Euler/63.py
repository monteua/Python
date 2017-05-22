'''
Powerful digit counts
Problem 63 
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

count = 0
for i in range(1, 10):
    for p in range(100):
        # calculate the power of i and p
        power = i ** p
        # if power have a same number of digits as the p
        if len(str(power)) == p:
            count += 1
print("Count:", count)

# one line solution
#print("Count:", sum([sum([1 for p in range(100) if len(str(i**p)) == p]) for i in range(1, 10)]))
