#import random module
import random

# use random function to get a number 
choice = random.choice(range(0,38))
print(choice)

# if statement that determinate wich color is the number on the roulette wheel
if choice % 2 == 0 and (12 <= choice <= 18) or choice % 2 == 0 and (30 <= choice <= 36) or choice % 2 != 0 and (1 <= choice <= 9) or choice % 2 != 0 and (19 <= choice <= 27):
    number = choice
    color = 'red'
elif choice % 2 == 0 and (2 <= choice <= 10) or choice % 2 != 0 and (11 <= choice <= 17) or choice % 2 == 0 and (20 <= choice <= 28) or choice % 2 != 0 and (29 <= choice <= 35):
    number = choice
    color = 'black'

# if statement that determinate if number will pay for odd or even
if choice % 2 == 0 and choice != 0:
    odd_even = 'even'
elif choice % 2 != 0 and choice != 37:
    odd_even = 'odd'

# if statement that determinate if 0 or 00 win (37 stand for 00)
if choice == 37:
    number = '00'
    choice == number
    color = 'green'
elif choice == 0:
    number = choice
    color = 'green'

# if statement that determinate wich range will pay (1 to 18 or 19 to 36), if so
if 1 <= choice <= 18:
    range_payout = '1 to 18'
elif 19 <= choice <= 36:
    range_payout = '19 to 36'

# if statement that print results on the screen
if number == 0 or number == '00':
    print('Pay ' + str(number) + '\n' + 'Pay ' + str(color))
else: 
    print('Pay ' + str(choice) + '\n' +  'Pay ' + str(color) + '\n' + 'Pay ' + str(odd_even) + '\n' + 'Pay '+ str(range_payout))

