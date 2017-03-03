'''
Write a Python program to find a missing number from a list.
Input : [1,2,3,4,6,7,8]
Output : 5
'''

def find_missing(lst):
    for i in range(1, max(lst)+1):
        if i not in lst:
            return i
print (find_missing([1,2,3,4,6,7,8]))
