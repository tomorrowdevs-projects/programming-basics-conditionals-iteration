import math

perimeter = 0
first_vertex_x = int(input('Enter the first x-coordinate:\n'))
first_vertex_y = int(input('Enter the first y-coordinate:\n'))
i = 0
h = 1
x_list = [first_vertex_x]
y_list = [first_vertex_y]

x = input('Enter the next x-coordinate (blank to quit):\n')
while x != ' ':
    x = int(x)
    x_list.append(x)
    y = int(input('Enter the next x-coordinate (blank to quit):\n'))
    y_list.append(y)
    if x_list[i] != x_list[h] and y_list[i] != y_list[h]:
        side = math.sqrt((x_list[h] - x_list[i])**2 + (y_list[h] - y_list[i])**2)
    else:
        if x_list[i] != x_list[h]:
            side = x_list[h] - x_list[i]
        else:
            side = y_list[h] - y_list[i]
    perimeter += side
    i += 1
    h += 1
    x = input('Enter the next x-coordinate (blank to quit):\n')
else:
    if first_vertex_x != x_list[i] and first_vertex_y != y_list[i]:
        side = math.sqrt((first_vertex_x - x_list[i])**2 + (first_vertex_y - y_list[i])**2)
    else:
        if first_vertex_x != x_list[i]:
            side = x_list[i] - first_vertex_x
        else:
            side = y_list[i] - first_vertex_y
    perimeter += side
print(perimeter)