integer_number = int(input('Enteran integer number greater than 2:\n'))
i = 2

if integer_number < 2:
    print('Only numbers greater than 2')

while integer_number > 2:
    if integer_number % i == 0:
        print(i)
        integer_number = integer_number // i
    else:
        i += 1