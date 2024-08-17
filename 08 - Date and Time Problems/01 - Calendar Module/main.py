import calendar

n = list(map(int, input().split()))

week_day = calendar.weekday(n[2], n[0], n[1])
dayName = calendar.day_name[week_day]
print(dayName.upper())
