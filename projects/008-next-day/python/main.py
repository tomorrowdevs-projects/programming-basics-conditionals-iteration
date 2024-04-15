year=int(input('Please, enter the year your interested in:'))
month=int(input('Please, enter the month your interested in:'))
day=int(input('Please, enter the day your interested in:'))

if day==28 and month==2: #check if the year is leap
    if year%400==0: #leap year
        next_day=29
        next_month=2
        next_year=year
    elif year%100==0: #not leap year
        next_day=1
        next_month=3
        next_year=year
    elif year%4==0: #leap year
        next_day=29
        next_month=2
        next_year=year
    else: #not leap year
        next_day=1
        next_month=3
        next_year=year
elif (str(month) in '11-4-6-9' and day==30) or (str(month) in '1-3-5-7-8-10' and day==31): #check if month must be changed
    next_day=1
    next_month=month+1
    next_year=year
elif month==12 and day==31: #check if year must be changed
    next_day=1
    next_month=1
    next_year=year+1
else: #generic case
    next_day=day+1
    next_month=month
    next_year=year

print('{}-{:02d}-{:02d}'.format(next_year,next_month,next_day))
