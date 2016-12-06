'''
Write a Python program to convert all units of time into seconds.
'''
def convertToSeconds(days, hours, minutes, seconds):
    return (days*24*60*60) + (hours*60*60) + seconds

if __name__ == "__main__":
    days = int(raw_input("Days: "))
    hours = int(raw_input("Hours: "))
    minutes = int(raw_input("Minutes: "))
    seconds = int(raw_input("Seconds: "))

    print "Total time in seconds:",convertToSeconds(days, hours, minutes, seconds)
