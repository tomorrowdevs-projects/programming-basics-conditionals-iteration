user_month = input('Enter a month:\n')

if user_month.lower() == 'february':
    print('28 or 29 days')
elif user_month.lower() == 'november' or user_month.lower() == 'april' or user_month.lower() == 'june' or user_month.lower() == 'september':
    print('30 days')
else:
    print('31 days')
