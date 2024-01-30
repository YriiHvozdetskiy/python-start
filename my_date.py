from datetime import date, time, datetime, timedelta

my_date = date(2100, 4, 15)
print(my_date.isocalendar())  # (year=2100, week=15, weekday=4)
my_iso = my_date.isocalendar()
print(my_iso.year)  # 2100

my_time = time(18, 10, 45)  # 18:10:45
print(my_time)

my_datetime = datetime(2024, 1, 23, 23, 2, 23)
print(my_datetime)  # 2024-01-23 23:02:23
print(my_datetime.now())  # поточна дата і час

date_str = '10/12/2222'
converted_date = datetime.strptime(date_str, '%d/%m/%Y')
print(converted_date)  # 2222-12-10 00:00:00

#  додавання/віднімання дати до/від вже існуючої
print(my_datetime.now() + timedelta(days=2))
print(converted_date - timedelta(days=13, hours=2))  # 2222-11-26 22:00:00
