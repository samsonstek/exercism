import datetime
def add(moment):
    added_gigasecond = datetime.timedelta(seconds=1000000000)
    new_time = moment + added_gigasecond
    return new_time

