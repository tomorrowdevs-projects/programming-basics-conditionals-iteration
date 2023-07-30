minutes = int(input('Enter the total minutes:\n'))
messages = int(input('Enter the total messages:\n'))

print("Base charge: 15.00€")

if minutes > 50:
    extra_minutes = (minutes - 50) * 0.25
    print(f"Extra minutes charge: {extra_minutes:.2f}€;")
else:
    extra_minutes = 0

if messages > 50:
    extra_messages = (messages - 50) * 0.15
    print(f"Extra messages charge: {extra_messages:.2f}€;")
else:
    extra_messages = 0

tax = ((15 + extra_messages + extra_minutes + 0.44) * 5) / 100
total_bill = 15 + extra_minutes + extra_messages + 0.44 + tax

print(
    f"911 fee: 0.44€;\n" \
    f"Tax: {tax:.2f}€;\n" \
    f"Total bill amount: {total_bill:.2f}€"
)