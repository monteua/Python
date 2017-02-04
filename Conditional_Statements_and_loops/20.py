'''
Write a Python program to find the average of three values.
Expected Output:

Input first number: 15
Input second number: 26
Input third number: 29
The median is 23.3
'''

numbers = [input("Input first number: "), input("Input second number: "), input("Input third number: ")]
numbers = [float(x) for x in numbers]
print ("The average is", round(sum(numbers)/len(list(numbers)), 1))
