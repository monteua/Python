'''
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given sting.
Return the n copies of the whole string if the length is less than 2.
'''

def string(s, n):
    if len(s) < 2:
        print s * n
    else:
        print s[:2] * n




if __name__ == '__main__':
    user_input = raw_input("Enter the string: ")
    user_number = int(raw_input('Enter the number: '))
    string(user_input, user_number)