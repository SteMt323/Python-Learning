### Dates ###
from datetime import datetime
from datetime import time
from datetime import date

# datetime
now = datetime.now()


timestamp = now.timestamp()

print(timestamp)

# Crear una nueva fecha


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
print_date(now)

year_2025 = datetime(2025, 1, 1)
print(year_2025)

# time
current_time = time(21,6,4)


print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# date
current_date = date(2024, 3, 20)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# this is easy .-.
# help me