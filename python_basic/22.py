'''
Write a Python program to count the number 4 in a given list.
'''

def count_4(lst):
    count = 0
    for i in lst:
        if i == 4:
            count += 1
    return count

if __name__ == '__main__':
    user_input = map(int, raw_input("Enter the sequence of number separated by space: ").split(" "))
    print count_4(user_input)