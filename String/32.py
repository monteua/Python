'''
Write a Python program to display a number with a comma separator.
'''

x = 31415926
y = 129999

print "Original number:", x
print "New number:", '{:,}'.format(x)

print "Original number:", y
print "New number:", '{:,}'.format(y)