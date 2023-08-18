import random 

def coin_flip():
    outcomes = []
    consecutive_count = 0
    flips = 0

    while consecutive_count < 3: 
        outcome = random.choice(['H', 'T'])
        outcomes.append(outcome)
        
        if len(outcomes) >= 3 and all(outcome == outcomes[-1] for outcome in outcomes[-3:]):
            consecutive_count = 3
        else: 
            consecutive_count = 0
        
        flips += 1
    
    return " ".join(outcomes), flips


num_simulations = 10
total_flips = 0

for outcomes in range(num_simulations):
    
    outcomes, flips = coin_flip()
    total_flips += flips
    print(outcomes, f'({flips} flips)')

average = total_flips / num_simulations

print(f'\nOn average, {average} flips were needed')