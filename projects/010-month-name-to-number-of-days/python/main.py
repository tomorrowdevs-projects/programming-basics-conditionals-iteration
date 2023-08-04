# ask to user a month
month = input('Type a month please: ').lower()

# check if month is 30, 31, 28 or 29 days longer and print answer on the screen
if month == 'february':
    result = '28 or 29 days'     
elif month == 'april' or month == 'june' or month == 'september' or month == 'november':
    result = 30
elif month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
    result = 31    
else:
    result = 'Not valid input'

print(result)