#ask to user a day and a month
month = input('type a month: ').capitalize()
day = int(input('type a day: '))
   

# if else statements that returns the zodiacal sign by comparing the day typed by user with a range of numbers and the month typed with a string
if 22 <= day <= 31 and month == 'December' or 1 <= day <= 19 and month == 'January':
    sign = 'Capricorn'
elif 20 <= day <= 31 and month == 'January' or 1 <= day <= 18 and month == 'February':
    sign = 'Aquarius'
elif 19 <= day <= 28 and month == 'February' or 1 <= day <= 20 and month == 'March':
     sign = 'Pisces'
elif 21 <= day <= 31 and month == 'March' or 1 <= day <= 19 and month == 'April':
    sign = 'Aries'
elif 20 <= day <= 30 and month == 'April' or 1 <= day <= 20 and month == 'May':
    sign = 'Taurus'
elif 21 <= day <= 31 and month == 'May' or 1 <= day <= 20 and month == 'June':
     sign = 'Gemini'
elif 21 <= day <= 30 and month == 'June' or 1 <= day <= 22 and month == 'July':
    sign = 'Cancer'
elif 23 <= day <= 31 and month == 'July' or 1 <= day <= 22 and month == 'August':
     sign = 'Leo'    
elif 23 <= day <= 31 and month == 'August' or 1 <= day <= 22 and month == 'September':
     sign = 'Virgo'
elif 23 <= day <= 30 and month == 'September' or 1 <= day <= 22 and month == 'October':
     sign = 'Libra'     
elif 23 <= day <= 31 and month == 'October' or 1 <= day <= 21 and month == 'November':
    sign = 'Scorpio'
elif 22 <= day <= 30 and month == 'November' or 1 <= day <= 21 and month == 'December':
    sign = 'Sagittarius'

print(sign)