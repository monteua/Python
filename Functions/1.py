'''
Write a Python function to find the Max of three numbers.
'''

def max_of_three(num1, num2, num3):
    return max([num1, num2, num3])

numbers = input("Enter the three numbers separated by space:").split()

print ("Max of three:", max_of_three(numbers[0], numbers[1], numbers[2]))