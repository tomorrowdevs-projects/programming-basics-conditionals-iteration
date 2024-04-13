month=input('Please, enter your birth month:').lower()
day=int(input('Please, enter your birth day:'))

if month=='january' and day<=19:
    sign='capricorn'
elif month=='january' and day>19:
    sign='aquarius'
elif month=='february' and day<=18:
    sign='aquarius'
elif month=='february' and day>18:
    sign='pisces'
elif month=='march' and day<=20:
    sign='pisces'
elif month=='march' and day>20:
    sign='aries'
elif month=='april' and day<=19:
    sign='aries'
elif month=='april' and day>19:
    sign='taurus'
elif month=='may' and day<=20:
    sign='taurus'
elif month=='may' and day>20:
    sign='gemini'
elif month=='june' and day<=20:
    sign='gemini'
elif month=='june' and day>20:
    sign='cancer'
elif month=='july' and day<=22:
    sign='cancer'
elif month=='july' and day>22:
    sign='leo'
elif month=='august' and day<=22:
    sign='leo'
elif month=='august' and day>22:
    sign='virgo'
elif month=='september' and day<=22:
    sign='virgo'
elif month=='september' and day>22:
    sign='libra'
elif month=='october' and day<=22:
    sign='libra'
elif month=='october' and day>22:
    sign='scorpio'
elif month=='november' and day<=21:
    sign='scorpio'
elif month=='november' and day>21:
    sign='sagittarius'
elif month=='december' and day<=21:
    sign='sagittarius'
else:
    sign='capricorn'

print('Your astrological sign is {}'.format(sign))