while True:
    integer_number = int(input('Enter an integer number (0 to quit):\n'))
    if integer_number == 0:
        break

    sequence = [integer_number]
    while integer_number != 1:
        if integer_number % 2 == 0:
            integer_number = integer_number // 2
        else:
            integer_number = integer_number * 3 + 1

        sequence.append(integer_number)

    print(sequence)