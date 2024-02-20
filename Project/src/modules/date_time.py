import datetime


def date_time():
    date_time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return date_time_now
