year=int(input('Please, enter the year your interested in:'))
month=int(input('Please, enter the month your interested in:'))
day=int(input('Please, enter the day your interested in:'))

if month==2:
    if year%400==0: #leap year
        leap_year=True
    elif year%100==0: #not leap year
        leap_year=False
    elif year%4==0: #leap year
        leap_year=True
    else: #not leap year
        leap_year=False
    
    if leap_year:
        if day>29:
            print('Plese enter an existing date')
        elif day<29:
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1
            next_month=month+1
            next_year=year
    else:
        if day>28:
            print('Plese enter an existing date')
        elif day<28:
            next_day=day+1
            next_month=month
            next_year=year
        else:
            next_day=1
            next_month=month+1
            next_year=year
elif month==11 or month==4 or month==6 or month==9:
    if day>30:
        print('Plese enter an existing date')
    elif day<30:
        next_day=day+1
        next_month=month
        next_year=year
    else:
        next_day=1
        next_month=month+1
        next_year=year
else:
    if day>31:
        print('Plese enter an existing date')
    elif day<31:
        next_day=day+1
        next_month=month
        next_year=year
    else:
        next_day=1
        next_month=month+1
        next_year=year

print('{}-{:02d}-{:02d}'.format(next_year,next_month,next_day))
