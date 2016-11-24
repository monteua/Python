'''
Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

def checkval(num, lst):

    if num in lst:
        return True
    else:
        return False


if __name__ == '__main__':

    print checkval(3, [1, 5, 8, 3])
    print checkval(-1, [1, 5, 8, 3])