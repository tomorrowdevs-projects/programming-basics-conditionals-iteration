import random

max = 0
for number in range(1,100):
    number = random.randrange(1,100)
    if number > max:
        max = number 
        print(number, '<== Update')
    else:
        print(number)



