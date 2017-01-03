'''
Write a Python program to print the following floating numbers with no decimal places.
'''

x = 3.1415926
y = -12.9999

print "Original number:", x
print "New number:", '{:.0f}'.format(x)

print "Original number:", y
print "New number:", '{:.0f}'.format(y)