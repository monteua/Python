'''
Write a Python program to count the number of even and odd numbers from a series of numbers.
'''

odd = 0
even = 0

user_input = input("Enter the series of numbers: ")

for i in user_input.split():
    try:
        i = int(i)
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    except:
        continue
print ("Odd numbers: ", odd)
print ("Even numbers: ", even)