# ask to user column and row 
user_input = input('Type a position of chess board: ')

# iterate user input to divide column and row
for i in user_input:
    if i.isalpha():
        col = i.lower()
    if i.isdigit():
        row = int(i)


# storing in a variable a string with the letters of the column that start with a white or black square
start_black = 'aceg'
start_white = 'bdfh'

# if statement that determinate output on the basis of wich color is the square choosed, also check if input is valid
if len(user_input) != 2 or 1 < row > 8 or (col not in start_white and col not in start_black):
    result = "an invalid input"
elif col in start_black and row % 2 == 0:
    result = 'white'
elif col in start_black and row % 2 > 0:
    result = 'black'
elif col in start_white and row % 2 == 0:
    result = 'black'
elif col in start_white and row % 2 > 0:
    result = 'white'

print(f'the {user_input} is {result}')