
u_year = input('Insert year: ')
u_year = int(u_year)

u_month = input('Insert month: ')
u_month = int(u_month)

u_day = input('Insert day: ')
u_day = int(u_day)

if u_year % 400 == 0:                           # leap years
    leap_year = 1

elif u_year % 100 == 0:
    leap_year = 0

elif u_year % 4 == 0:
    leap_year = 1

else:
    leap_year = 0

if (u_month == 1 or                             # 31 days months
    u_month == 3 or
    u_month == 5 or
    u_month == 7 or
    u_month == 8 or
    u_month == 10 or
    u_month == 12
    ):
    
    if u_day == 31 and u_month == 12:
        nx_day = 1
        nx_month = 1
        nx_year = u_year + 1

    elif u_day == 31:
        nx_day = 1
        nx_month = u_month + 1
        nx_year = u_year

    else:
        nx_day = u_day +1
        nx_month = u_month
        nx_year = u_year

elif u_month == 2 and leap_year == 1:           # February leap years
    
    if u_day == 29:
        nx_day = 1
        nx_month = u_month + 1
        nx_year = u_year
    
    else:
       nx_day = u_day +1
       nx_month = u_month
       nx_year = u_year

elif u_month == 2 and leap_year == 0:           # February no leap
    
    if u_day == 28:
        nx_day = 1
        nx_month = u_month + 1
        nx_year = u_year
    
    else:
       nx_day = u_day +1
       nx_month = u_month
       nx_year = u_year

else:                                           # 30 days month
    if u_day == 30:
        nx_day = 1
        nx_month = u_month + 1
        nx_year = u_year

    else:
        nx_day = u_day +1
        nx_month = u_month
        nx_year = u_year


print(f'The user selected date is {u_year}-{u_month:02d}-{u_day:02d}, the next day is {nx_year}-{nx_month:02d}-{nx_day:02d}')
