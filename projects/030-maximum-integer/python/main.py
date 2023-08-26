import random

maximum_number = random.choice(range(1, 101))
print(maximum_number, '<== Update')
i = 1

while maximum_number != 100:
    new_number = random.choice(range(1, 101))

    if new_number > maximum_number:
        maximum_number = new_number
        print(maximum_number, '<== Update')
        i += 1
    else:
        print(new_number)

print(f'The maximum value found was {maximum_number}')
print(f'The maximum value was updated {i} times')
