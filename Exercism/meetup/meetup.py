import datetime


def meetup_day(year, month, weekday, numday):
    which_day = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last': -1}

    weekdays = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [],
                'Friday': [], 'Saturday': [], 'Sunday': []}

    current_date = datetime.date(year, month, 1)

    while current_date.month == month:
        day_name = current_date.strftime("%A")
        weekdays[day_name].append(current_date.day)
        current_date += datetime.timedelta(days=1)

    if numday in which_day:
        idx = which_day[numday]
        return datetime.date(year, month, weekdays[weekday][idx])
    elif numday == 'teenth':
        return datetime.date(year, month, [d for d in weekdays[weekday] if 12 < d < 20][0])

