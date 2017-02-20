'''
Write a Python program of recursion list sum.
Test Data : [1, 2, [3,4], [5,6]]
Expected Result : 21
'''

def recursion(lst):
    s = 0

    for i in lst:
        if len(str(i)) == 1:
            s += int(i)
        else:
            s += sum(map(int, i))
    return s

print (recursion([1, 2, [3,4], [5,6]]))