year=int(input('Please, enter the year your interested in:'))

if year%400==0:
    print('{} is a leap year'.format(year))
elif year%100==0:
    print('{} is not a leap year'.format(year))
elif year%4==0:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))