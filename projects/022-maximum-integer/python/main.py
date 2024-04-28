from random import randrange

while True:
    max=int(input('Please, insert a positive integer between 1 and 100:'))
    if max<1 or max>100:
        print('You have insert an invalid integer, try again or press ctrl+c to quit')
    else:
        break
print('{} <== Update'.format(max))
counter=0
updates_number=0
while counter<100:
    number=randrange(1,100,1)
    if number>max:
        max=number
        updates_number+=1
        print('{} <== Update'.format(max))
    else:
        print(number)
    counter+=1

print('The maximum value found was {}'.format(max))
print('The maximum value was updated {} times'.format(updates_number))