guest = input('Enter the age (newline character to quit):\n')
price = 0

while guest != '':
    guest = int(guest)
    if guest in range(3, 13):
        price += 14
    elif guest >= 65:
        price += 18
    elif guest <= 2:
        price += 0
    else:
        price += 23

    guest = input('Enter the age (newline character to quit):\n')
print("Total price of admission: $""{:.2f}".format(price))