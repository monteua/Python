'''
Write a Python program to solve the Fibonacci sequence using recursion
'''

def fibonacci(number):
    if number == 1 or number == 2:
        return 1
    else:
        return (fibonacci(number-1) + fibonacci(number - 2))

print (fibonacci(13))
print (fibonacci(7))