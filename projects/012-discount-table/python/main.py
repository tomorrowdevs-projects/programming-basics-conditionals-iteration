for price in (4.95, 9.95, 14.95, 19.95, 24.95):
    discount=price*60/100
    new_price=price-discount
    print(f"Original price: {price}")
    print(f"Discount amount: {discount:.2f}")
    print(f"New price: {new_price:.2f}")