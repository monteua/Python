'''
Write a Python program that accepts a string and calculate the number of digits and letters.
'''

while True:
    user_input = input("Enter the string:")

    letter_count = 0
    number_count = 0

    if user_input:
        for i in user_input:
            if i.isalpha():
                letter_count += 1
            elif i.isdigit():
                number_count += 1
    else:
        break
    print ("Letters:", letter_count)
    print ("Digits:", number_count)