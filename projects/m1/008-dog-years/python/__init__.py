human_age = int(input('Enter human age:\n'))
dog_years = 0

while human_age < 0:
    print('Enter only positive numbers!')
    print(human_age)
    human_age = int(input('Enter human age:\n'))

if human_age > 2:
    dog_years = 21
    i = 3
    while i != human_age:
        i += 1
        dog_years += 4
    else:
        dog_years += 4
else:
    dog_years = int(10.5 * human_age)

print(f'Here is the conversion:\n{human_age} human years = {dog_years} dog years')