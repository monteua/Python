'''
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''

def intCompare(int1, int2):

    if int1 == int2 or int1 + int2 == 5 or int1 - int2 == 5:
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        print intCompare(int(raw_input("First number: ")), int(raw_input("Second number: ")))