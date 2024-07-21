import math

new_distance = 0
x1 = float(input('Enter the first x-coordinate:'))
y1 = float(input('Enter the first y-coordinate:'))

x2 = (input('Enter the next x-coordinate:'))

while x2 != '':
    x2 = float(x2)
    y2 = float(input('Enter the next y-coordinate:'))
    
    distance = math.sqrt((x2 - (x1))**2 + (y2 - (y1))**2) 
    new_distance = new_distance + distance

    x1 = x2
    y1 = y2

    x2 = (input('Enter the next x-coordinate:'))


print(f'The perimeter of that polygon is {new_distance}')