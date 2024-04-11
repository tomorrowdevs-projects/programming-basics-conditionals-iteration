#--REQUIREMENTS--#
# 1) take use input
# 2) save it in a variable
# 3) check if the input is a month with 31, 30 or 28/29 days
# 4) print the number of days of the month

month=input('Please write the name of a month:').lower()
months='january-february-march-april-may-june-july-august-september-october-november-december'
months30='november-april-june-september'
if not (month in months):
    print('You have typed a wrong name, please restart the app and write the name of the month in the right way')
elif month in months30:
    print('30 days')
elif month=='february':
    print('28 or 29 days')
else:
    print('31 days')