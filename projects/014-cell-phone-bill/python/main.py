#ask to user total minutes and messanges for the bill
minutes = int(input('Type total minutes: '))
messages = int(input('Type total messages: '))
# define a variable with the price of base bill and extra charge for 911 calls
base_bill = 15
fee_911 = 0.44

#adding costs to total
total = base_bill + fee_911
print('Base charge: ' + '{:.2f}'.format(base_bill) + '€')

# print on screen costs for extra messages and extra minutes
if minutes > 50:
    costs_extra_minutes = (minutes - 50) * 0.25
    total += costs_extra_minutes
    print('Extra minutes charge: ' + '{:.2f}'.format(costs_extra_minutes) + '€')

if messages > 50:
    costs_extra_messages = (messages - 50) * 0.15
    total += costs_extra_messages
    print('Extra messages charge: ' + '{:.2f}'.format(costs_extra_messages) + '€')

print('911 fee: ' + '{:.2f}'.format(fee_911) + '€')

sales_tax = total * 5 / 100

print('Tax: ' + '{:.2f}'.format(sales_tax) + '€')

total += sales_tax

print('Total bill amount: ' + '{:.2f}'.format(total) + '€')




