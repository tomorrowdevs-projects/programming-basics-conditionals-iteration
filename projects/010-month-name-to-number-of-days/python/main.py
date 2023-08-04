# ask to user a month
month = input('Type a month please: ').lower()

# declare two variables where store months's names divided by their lenght 
months_30 = 'apriljuneseptembernovember'
months_31 = 'januarymarchmayjulyaugustoctoberdecember'

# check if month is 30, 31, 28 or 29 days longer and print answer on the screen
if month == 'february':
    result = '28 or 29 days'     
elif month in months_30:
    result = 30
elif month in months_31:
    result = 31    
else:
    result = 'Not valid input'

print(result)