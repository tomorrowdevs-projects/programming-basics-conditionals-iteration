price_1=4.95
price_2=9.95
price_3=14.95
price_4=19.95
price_5=24.95

labels=''

for j in range(1,6):
    price=eval('price_{}'.format(j))
    discount=round(price*0.6,2)
    discounted_price=round(price-discount,2)
    labels=labels+'{}\n{}\n{}\n\n'.format(price,discount,discounted_price)

print(labels)


