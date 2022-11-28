import datetime


def year():
    years = datetime.datetime.today()
    years = years.strftime("%Y")
    return int(years)


def year2():
    years = datetime.datetime.today()
    years = years.strftime("%y")
    return int(years)
