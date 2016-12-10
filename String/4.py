'''
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to
'$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''

user_input = raw_input("Enter the string: ")
lst = list()
for i in user_input:
    lst.append(i)

first = user_input[0]
for n, i in enumerate(lst):
    if i == first:
        lst[n] = '$'
lst[0] = first


print "".join(lst)