from datetime import timedelta

def add_gigasecond(date):
    time = timedelta(seconds=10**9)
    return time+date
