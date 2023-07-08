user_birthday = input('Enter the day and month:\n').split(' ')

month = user_birthday[1]
day = int(user_birthday[0])


if month.lower() == 'january' and day in range(1, 20) or month.lower() == 'december' and day in range(1, 23):
    print('Capricorn')
elif month.lower() == 'january' and day in range(20, 32) or month.lower() == 'february' and day in range(1, 19):
    print('Aquarius')
elif month.lower() == 'february' and day in range(19, 30) or month.lower() == 'march' and day in range(1, 21):
    print('Pisces')
elif month.lower() == 'march' and day in range(21, 32) or month.lower() == 'april' and day in range(1, 20):
    print('Aries')
elif month.lower() == 'april' and day in range(20, 31) or month.lower() == 'may' and day in range(1, 21):
    print('Taurus')
elif month.lower() == 'may' and day in range(21, 32) or month.lower() == 'june' and day in range(1, 21):
    print('Gemini')
elif month.lower() == 'june' and day in range(21, 31) or month.lower() == 'july' and day in range(1, 23):
    print('Cancer')
elif month.lower() == 'july' and day in range(23, 32) or month.lower() == 'august' and day in range(1, 23):
    print('Leo')
elif month.lower() == 'august' and day in range(23, 32) or month.lower() == 'september' and day in range(1, 23):
    print('Virgo')
elif month.lower() == 'september' and day in range(23, 31) or month.lower() == 'october' and day in range(1, 23):
    print('Libra')
elif month.lower() == 'october' and day in range(23, 32) or month.lower() == 'november' and day in range(1, 22):
    print('Scorpio')
elif month.lower() == 'november' and day in range(22, 31) or month.lower() == 'december' and day in range(1, 22):
    print('Sagittarius')