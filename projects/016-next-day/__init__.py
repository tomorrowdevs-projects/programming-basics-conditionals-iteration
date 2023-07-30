user_year = int(input('Enter a year\n'))
user_month = int(input('Enter a month\n'))
user_day = int(input('Enter a day\n'))

if user_month % 2 != 0 and user_month != 11 or user_month == 8 or user_month == 12:
    #31 days max
    if user_day == 31 and user_month == 12:
        user_day = 1
        user_month = 1
        user_year += 1
    elif user_day == 31:
        user_day = 1
        user_month += 1
    else:
        user_day += 1

elif user_month % 2 == 0 and user_month != 2:
    #30 days max
    if user_day != 30:
        user_day +=1
    else:
        user_month += 1
        user_day = 1

#February
elif user_year % 400 == 0 or user_year % 4 == 0:
    #29 days max
    if user_day != 29:
        user_day += 1
    else:
        user_month += 1
        user_day = 1
else: #28 days max
    if user_day != 28:
        user_day += 1
    else:
        user_month += 1
        user_day = 1

print('The next day will be: {:02d}-{:02d}-{:02d}'.format(user_year, user_month, user_day))