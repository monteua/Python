'''
Write a Python program to find whether
a given number (accept from the user) is even or odd, print out an appropriate message to the user.
'''

def check_number(num):
    if num % 2 == 0:
        print num, "is even."
    else:
        print num, 'is odd.'


if __name__ == '__main__':
    user_input = raw_input("Enter the number: ")
    check_number(int(user_input))