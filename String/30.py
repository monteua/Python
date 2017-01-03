'''
Write a Python program to print the following floating numbers upto 2 decimal places with a sign
'''

x = 3.1415926
y = -12.9999

print "Original number:", x
print "New number:", '{:+.2f}'.format(x)

print "Original number:", y
print "New number:", '{:+.2f}'.format(y)