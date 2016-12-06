'''
Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

time_in_seconds = int(raw_input("Enter the time in seconds: "))

# converting the time from seconds
days = int(time_in_seconds / 3600 / 24)
hours = int((time_in_seconds - days*3600*24)/3600)
minutes = int((time_in_seconds - days*3600*24 - hours*3600))/60
seconds = int(time_in_seconds - days*3600*24 - hours*3600 - minutes*60)

print days, 'day(s)', hours, 'hour(s)', minutes, 'minute(s)', seconds, 'second(s)'