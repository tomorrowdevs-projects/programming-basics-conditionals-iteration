# ask to user a year
year = int(input("Type a year: "))

# determinate if the year typed by user is a leap year or not and print result
if year % 400 == 0 or year % 100 == 0 or year % 4 == 0:
    print('is a leap year')
else:
    print('is not a leap year')