sequence = ''
user_input = None
result = ''

while user_input != 0:
    user_input = input('type a positive number or 0 to end: ')
    if user_input == '':
        print('Empty field')
    elif user_input.isnumeric() == False:
        print (f'"{user_input}" not valid value')
    else:
        user_input = int(user_input)
        number = user_input
        sequence = str(number) 
        if user_input != 0:
            while number != 1:
                if number % 2 == 0:
                    number = number // 2
                    sequence += f' {number}'
                else:
                    number = number * 3 + 1
                    sequence += f' {number}'
            result += f'{sequence} \n'
print(result[:len(result)-1])
