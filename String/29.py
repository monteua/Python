'''
Write a Python program to print the following floating numbers upto 2 decimal places.
'''

x = 3.1415926
y = 12.9999

print "Original number:", x

# 1st  variant
print "New number:", round(x, 2)
# or
#print "New number:", '{:.2f}'.format(x)

print "Original number:", y
# 1st  variant
print "New number:", round(y, 2)
# or
#print "New number:", '{:.2f}'.format(y)