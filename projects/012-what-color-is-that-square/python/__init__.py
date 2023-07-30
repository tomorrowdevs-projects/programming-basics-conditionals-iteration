import string
i = 0

user_position = input('Enter the position:\n')
user_number = int(user_position[1])
user_letter = user_position[0].lower()

while string.ascii_lowercase[i] != user_letter:
    i += 1

if i % 2 != 0 and user_number % 2 == 0:
    square_color = 'Black'
elif i % 2 == 0 and user_number % 2 != 0:
    square_color = 'Black'
else:
    square_color = 'White'

print(square_color)
