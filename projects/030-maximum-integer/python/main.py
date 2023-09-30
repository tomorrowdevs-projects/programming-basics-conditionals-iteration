import random
# declare variable where store a random nuber between 1 and 100
high_number = random.choice(range(1,101))
# declare a variable where store numbers of updates
updates = 0
# for cycle that choose another random number, prints it and compares with the first one, if it's bigger prints a realative message, if not prints only the number and go on 100 times
for i in range(1,100):
    number = random.choice(range(1,101))
    if number > high_number:
        high_number = number
        print(f'{number} <== update')
        updates += 1
    else:    
        print(number)

print(f'The maximum value found was {high_number} \nThe maximum value was updated {updates} times ')