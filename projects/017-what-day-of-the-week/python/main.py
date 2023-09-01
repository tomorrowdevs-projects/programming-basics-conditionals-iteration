import math

year = int(input('Type a year:\n'))

day_of_the_week = math.floor((year + math.floor((year - 1) / 4) - math.floor((year - 1) / 100) + math.floor((year - 1) / 400)) % 7)
days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print(days_of_the_week[day_of_the_week])
