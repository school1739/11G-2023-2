import datetime
year=int(input())
month=int(input())
day=int(input())
tomorrow=datetime.date(year,month,day)+datetime.timedelta(weeks=1)
print(tomorrow)
