import random

maximum = random.randint(1, 100)
generated = []
counter_update = 0

print(maximum)

for n in range(99):
    generated.append(random.randint(1, 100))

for g in generated:
    
    if g > maximum:    
        maximum = g
        print(f'{g} <== Update')
        counter_update += 1
    
    else:
        print(g)

print(f'The maximum value found was {maximum}')
print(f'The maximum value was updated {counter_update} times')





