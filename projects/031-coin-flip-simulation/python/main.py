import random

coins = 'H', 'T'
number_of_flips = 0
for i in range(10):
    record = []
    heads = 0
    tails = 0


    while True:
        coin_flip = random.choice(coins)
        if coin_flip == 'T':
            heads += 1
            tails = 0
        else:
            heads = 0
            tails += 1
        record.append(coin_flip)

        if heads == 3 or tails == 3:
            number_of_flips += len(record)
            print(f"{'-'.join(record)} ({len(record)} flips)")
            break

average = number_of_flips / 10
print('\n'
    f'On average, {average} flips were needed')