# datetime is a built-in module in Python
# It provides classes for manipulating dates and times
from datetime import date

# Create dates
two_hurricanes_dates = [date(2016, 10, 7), date(2017, 6, 21)]
# Date's attributes
print(two_hurricanes_dates[0].year)  # 2016
print(two_hurricanes_dates[1].year)  # 2017
print(two_hurricanes_dates[0].month)  # 10
print(two_hurricanes_dates[1].month)  # 6
print(two_hurricanes_dates[0].day)  # 7
print(two_hurricanes_dates[1].day)  # 21
# Date's methods
print(two_hurricanes_dates[0].weekday())  # 0   # Monday
print(two_hurricanes_dates[1].weekday())  # 2   # Wednesday
print(two_hurricanes_dates[0].isoformat())  # 2016-10-07
print(two_hurricanes_dates[1].isoformat())  # 2017-06-21
print(two_hurricanes_dates[0].toordinal())  # 736891

# Math operations with dates
delta = two_hurricanes_dates[1] - two_hurricanes_dates[0]
