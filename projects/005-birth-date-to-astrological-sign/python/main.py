
u_month = input('Insert your birth month: ')
u_day = input('Insert your birth day: ')

month = u_month.lower()
day = int(u_day)

if month == 'december' and 22 <= day <= 31 or month == 'jenuary' and 1 <= day <= 19:
    print('Capricorn')

elif month == 'jenuary' and 20 <= day <= 31 or month == 'february' and 1 <= day <= 18:
    print('Aquarius')

elif month == 'february' and 19 <= day <= 29 or month == 'march' and 1 <= day <= 20:
    print('Pisces')

elif month == 'march' and 21 <= day <= 31 or month == 'april' and 1 <= day <= 19:
    print('Aries')

elif month == 'april' and 20 <= day <= 30 or month == 'may' and 1 <= day <= 20:
    print('Taurus')

elif month == 'may' and 21 <= day <= 31 or month == 'june' and 1 <= day <= 20:
    print('Gemini')

elif month == 'june' and 21 <= day <= 30 or month == 'july' and 1 <= day <= 22:
    print('Cancer')

elif month == 'july' and 23 <= day <= 31 or month == 'august' and 1 <= day <= 22:
    print('Leo')

elif month == 'august' and 23 <= day <= 31 or month == 'september' and 1 <= day <= 22:
    print('Virgo')

elif month == 'september' and 23 <= day <= 30 or month == 'october' and 1 <= day <= 22:
    print('Libra')

elif month == 'october' and 23 <= day <= 31 or month == 'november' and 1 <= day <= 21:
    print('Scorpio')

elif month == 'november' and 22 <= day <= 30 or month == 'december' and 1 <= day <= 21:
    print('Sagittarius')

else:
    print('wrong input')