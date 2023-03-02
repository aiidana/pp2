# from datetime import date, timedelta
# x=datetime.datetime.now()
# day= x- timedelta(5)
# print(date.today())
# print(day)
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)


# import datetime
# start_date = datetime.datetime.now()
# end_date = start_date - datetime.timedelta(days=5)