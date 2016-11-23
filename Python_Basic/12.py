'''
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
import calendar
print calendar.TextCalendar(calendar.MONDAY).prmonth(int(raw_input("Year: ")), int(raw_input("Month: ")))