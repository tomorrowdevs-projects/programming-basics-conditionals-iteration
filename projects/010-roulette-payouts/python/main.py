import random

spaces = ['00', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

result = random.choice(spaces)
print (f'The spin resulted in {result}')

if result == 0:                                 # check 0, 00 or single number
    print('Pay 0')
    exit()

elif result == '00':
    print('Pay 00')
    exit()

else:
    print(f'Pay {result}')


if result in red:                               # check red or black
    print('Pay Red')

else:
    print('Pay Black')


if result % 2 == 0:                             # check even or odd
    print('Pay Even')

else:
    print('Pay Odd')


if result <= 18:                                # check 1 to 18 or 19 to 36
    print('Pay 1 to 18')

else:
    print('Pay 19 to 36')



