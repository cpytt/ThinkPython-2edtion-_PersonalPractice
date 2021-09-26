import time

print(time.time())

minutes = time.time() // 60
hours = minutes // 60
days = hours // 24
years = days // 365

seconds_real = time.time() % 60
minutes_real = minutes % 60
hours_real = hours % 24

print('minutes = ', minutes)
print('hours = ', hours)
print('days = ', days)
print('years = ', years)

print('time =', int(hours_real), ':', int(minutes_real), ':', int(seconds_real))
