import random

coin_face = ['H','T']
coin_toss = []
toss_number = []
simulation = 1
flip_counter = 1
consecutive_counter = 1

while simulation <= 10:

    first_flip = random.choice(coin_face)
    coin_toss.append(first_flip)
    
    while consecutive_counter < 3:
        flip_coin = random.choice(coin_face)
        flip_counter += 1
        
        if flip_coin == first_flip:
            coin_toss.append(flip_coin)
            consecutive_counter +=1
        
        else:
            coin_toss.append(flip_coin)
            first_flip = flip_coin
            consecutive_counter = 1
            
    toss_number.append(len(coin_toss))
    print(*coin_toss, f'({flip_counter} flips)')
    
    coin_toss.clear()
    simulation += 1
    flip_counter = 1
    consecutive_counter = 1

flip_avarage = (sum(toss_number)) / 10
print(f'On avarage, {flip_avarage} flips were needed')



