
import math

perimeter = 0

first_x = float(input('Enter the first x-coordinate: '))
first_y = float(input('Enter the first y-coordinate: '))

x = first_x
y = first_y

next_x = ' '

while next_x != '':
    next_x = input('Enter the next x-coordinate: ')
    if next_x != '':
        next_x = float(next_x)
        next_y = float(input('Enter the next y-coordinate: '))
        distance = math.sqrt((next_x - x)**2 + (next_y - y)**2)
        perimeter = perimeter + distance
        x = next_x
        y = next_y
    else:
        distance = math.sqrt((x - first_x)**2 + (y - first_y)**2)
        perimeter = perimeter + distance

print(f'The perimeter of that polygon is {perimeter}')