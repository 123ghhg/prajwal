import time
from datetime import datetime as dt
import datetime
time_obj =time.localtime()
current_time = time.strftime("%H:%M:%S", time_obj)
print("current date and time",current_time,"and",dt.date(dt.now()))
print("current year: ", datetime.date.today().strftime("%Y"))
print("month of year: ",datetime.date.today().strftime("%B"))
print("week number of the year:", datetime.date.today().strftime("%W"))
print("weekday of the week:", datetime.date.today().strftime("%w"))
print("day of year:",datetime.date.today().strftime("%j"))
print("day of the month:", datetime.date.today().strftime("%d"))
print("day of week:",datetime.date.today().strftime("%A"))
