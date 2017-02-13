'''
Write a Python script to display the -
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
'''

import datetime

print ("a) Current date and time:", datetime.datetime.today())
print ("b) Current year:", datetime.datetime.today().year)
print ("c) Month of year:", datetime.datetime.today().strftime("%B"))
print ("d) Week number of the year:", datetime.datetime.today().strftime("%W"))
print ("e) Weekday of the week:", datetime.datetime.today().strftime("%w"))
print ("f) Day of year:", datetime.datetime.today().strftime("%j"))
print ("g) Day of the month:", datetime.datetime.today().strftime("%d"))
print ("h) Day of week:", datetime.datetime.today().strftime("%A"))