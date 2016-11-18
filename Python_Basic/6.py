'''
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple
with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

user_data = raw_input('Enter a sequence of comma-separated numbers: ').strip().split(',')
print "List:", user_data
print 'Tuple:', tuple(user_data)
