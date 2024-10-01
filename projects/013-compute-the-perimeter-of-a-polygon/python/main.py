from math import sqrt

x_coordinate=input("Enter the first x-coordinate: ")
y_coordinate=input("Enter the first y-coordinate: ")
perimeter=0

next_x_coordinate=input("Enter the next x-coordinate (blank to quit): ")
while next_x_coordinate != "":
    next_y_coordinate=input("Enter the next y-coordinate: ")

    distance = sqrt((float(x_coordinate)-float(next_x_coordinate))**2+(float(y_coordinate)-float(next_y_coordinate))**2)
    perimeter += distance

    x_coordinate = next_x_coordinate
    y_coordinate = next_y_coordinate

    next_x_coordinate=input("Enter the next x-coordinate (blank to quit): ")

print(f"Perimeter: {perimeter:.2f}")   















