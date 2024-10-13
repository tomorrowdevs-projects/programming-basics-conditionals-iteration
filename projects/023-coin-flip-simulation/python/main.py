import random
NUMBER_OF_EXTRACTIONS=10
coin_faces=["H","T"]
flips_counter=0

for i in range(NUMBER_OF_EXTRACTIONS):
    stringa=""
    coin_flip_count=0
    tree_consecutive_coin=False
    
    while not(tree_consecutive_coin):
        coin_flip=random.choice(coin_faces)
        print(coin_flip, end=" ")
        coin_flip_count+=1
        stringa+=coin_flip

        if len(stringa)>=3 and stringa[-1]==stringa[-2]==stringa[-3]:
            print(f"({coin_flip_count} flips)")
            flips_counter+=coin_flip_count
            tree_consecutive_coin=True

average=flips_counter/NUMBER_OF_EXTRACTIONS
print(f"On average, {average} flips were needed.")