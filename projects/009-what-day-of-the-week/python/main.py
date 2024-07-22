import math
year=int(input("Year:"))

day_of_the_week=(year+math.floor((year-1)/4)-math.floor((year-1)/100)+math.floor((year-1)/400))%7

if day_of_the_week==0:
    day_of_the_week="Sunday"
    
elif day_of_the_week==1:
    day_of_the_week="Monday"
    
elif day_of_the_week==2:
    day_of_the_week="Tuesday"
    
elif day_of_the_week==3:
    day_of_the_week="Wednesday"
    
elif day_of_the_week==4:
    day_of_the_week="Thursday"
    
elif day_of_the_week==5:
    day_of_the_week="Friday"
    
else:
    day_of_the_week="Saturday"

print(f"{year}: {day_of_the_week}")