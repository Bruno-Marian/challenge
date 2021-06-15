import datetime


def get_diretory():
    data = datetime.datetime.today()
    return f'./{data.year}/{data.month}/{data.day}/{data.hour}/{data.minute}'
