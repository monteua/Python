'''
Write a Python function that takes a list of words and returns the length of the longest one
'''

def longest(lst):
    longest_so_far = ""
    for i in lst:
        if len(i) > len(longest_so_far):
            longest_so_far = i
    return longest_so_far



lst = ['one', 'two', 'three', 'four', 'five', 'six', 'sixteen']
print "Longest word:",longest(lst)
print len(longest(lst)), 'characters.'