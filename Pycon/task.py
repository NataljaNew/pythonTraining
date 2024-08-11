from datetime import datetime
from calendar import monthrange

year, month = int(input()), int(input())
num_days = monthrange(year, month)
count = 0
for day in range(1,num_days[1]+1):
    date = datetime(year, month, day)
    if date.weekday() == 3:
        count += 1
    if count == 4:
        print(date.strftime('%d.%m.%Y'))
        break
