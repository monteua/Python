'''
Write a Python program to find missing numbers from a list.
Input : [1,2,3,4,6,7,10]
Output : [5, 8, 9]
'''

def find_missing(lst):
    missing = []
    for i in range(1, max(lst)+1):
        if i not in lst:
            missing.append(i)
    return missing
print (find_missing([1,2,3,4,6,7,10]))