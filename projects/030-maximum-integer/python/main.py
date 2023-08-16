import random

count_update = 0
max = 0
for number in range(1,100):
    number = random.randrange(1,100)
    if number > max:
        max = number 
        count_update += 1
        print(number, '<== Update')
    else:
        print(number)

print(f'The maximum value found was {max}')
print(f'The maximum value was updated {count_update} times')



