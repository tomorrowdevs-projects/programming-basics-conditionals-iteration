
u_minutes = input('Insert number of minutes used this month: ')
u_minutes = int(u_minutes)

u_messages = input('Insert number of message used this month: ')
u_messages = int(u_messages)

base_charges = 15
minutes_charge = 0
message_charge = 0
emergency_fee = 0.44


print(f'Base charge: {base_charges:>15.2f}€')

if u_minutes > 50:
    minutes_charge = (u_minutes - 50) * 0.25
    print(f'Extra minutes charge: {minutes_charge:>5.2f}€')

else:
    pass

if u_messages > 50:
    message_charge = (u_messages - 50) * 0.15
    print(f'Extra messages charge: {message_charge:.2f}€')

else:
    pass

print(f'911 fee: {emergency_fee:>18.2f}€')

tax = (base_charges + minutes_charge + message_charge + emergency_fee) * 0.05
print(f'Tax: {tax:>22.2f}€')
print(f'Total bill amount: {base_charges + minutes_charge + message_charge + emergency_fee + tax:>9.2f}€')

