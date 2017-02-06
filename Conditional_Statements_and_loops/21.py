'''
Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
'''

numbers = []

while True:
    user_input = input("Enter the numbers, input 0 to finish: ")
    try:
        user_input = float(user_input)
        if user_input == 0:
            break
        else:
            numbers.append(user_input)
    except:
        print ("Not a number!")

print ("Sum:", round(sum(numbers)), 2)
print ("Avg:", round((sum(numbers)/len(numbers)), 2))