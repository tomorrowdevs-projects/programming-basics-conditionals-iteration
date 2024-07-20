minutes=int(input("Minutes:"))
messages=int(input("Messages:"))

BASE_CHARGE=15.00
ADDITIONAL_911_CHARGE=0.44

print(f"Base charge: {BASE_CHARGE:.2f}€")

extra_minutes_charge=0
if minutes>50:
    extra_minutes_charge=(minutes-50)*0.25
    print(f"Extra minutes charge: {extra_minutes_charge:.2f}€")

extra_messages_charge=0
if messages>50:
    extra_messages_charge=(messages-50)*0.15
    print(f"Extra messages charge: {extra_messages_charge:.2f}€")

print(f"911 fee: {ADDITIONAL_911_CHARGE:.2f}€")

tax=(BASE_CHARGE+extra_minutes_charge+extra_messages_charge+ADDITIONAL_911_CHARGE)*5/100
print(f"Tax: {tax:.2f}€")

total_bill_amount=BASE_CHARGE+extra_minutes_charge+extra_messages_charge+ADDITIONAL_911_CHARGE+tax
print(f"Total bill amount: {total_bill_amount:.2f}€")