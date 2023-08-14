user_year = int(input('Enter a year:\n'))

if user_year % 400 == 0:
    print(user_year, 'is a leap year')
elif user_year % 100 == 0:
    print(user_year, 'is not a leap year')
elif user_year % 4 == 0:
    print(user_year, 'is a leap year')
else:
    print(user_year, 'is not a leap year')
