original_price = [4.95, 9.95, 14.95, 19.95, 24.95]
print('|  Original price | Discount  | New price  |')
print('---------------------------------------------------')

for price in original_price:
    new_price = (price * 60) / 100
    discount = price - new_price
    print("|    {:.2f}$        |  {:.2f}$   |    {:.2f}$    |".format(price, discount, new_price))
    print('---------------------------------------------------')