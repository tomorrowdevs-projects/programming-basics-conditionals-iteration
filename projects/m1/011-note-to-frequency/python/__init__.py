user_note = input('Enter a note:\n')
letter = user_note[0]
number = int(user_note[1])
i = number
if letter.upper() == 'C' and number in range(0, 9):
    frequency = 261.63
    if number > 4:
        i = 4
        while i != number:
            frequency *= 2
            i += 1
    elif number < 4:
        i = 4
        while i != number:
            frequency /= 2
            i -= 1

elif letter.upper() == 'D' and number in range(0, 9):
    frequency = 293.66
    if number > 4:
        i = 4
        while i != number:
            frequency *= 2
            i += 1
    elif number < 4:
        i = 4
        while i != number:
            frequency /= 2
            i -= 1

elif letter.upper() == 'E' and number in range(0, 9): 
    frequency = 329.63
    if number > 4:
        i = 4
        while i != number:
            frequency *= 2
            i += 1
    elif number < 4:
        i = 4
        while i != number:
            frequency /= 2
            i -= 1

elif letter.upper() == 'F' and number in range(0, 9): 
    frequency = 349.23
    if number > 4:
        i = 4
        while i != number:
            frequency *= 2
            i += 1
    elif number < 4:
        i = 4
        while i != number:
            frequency /= 2
            i -= 1

elif letter.upper() == 'G' and number in range(0, 9): 
    frequency = 392
    if number > 4:
        i = 4
        while i != number:
            frequency *= 2
            i += 1
    elif number < 4:
        i = 4
        while i != number:
            frequency /= 2
            i -= 1

elif letter.upper() == 'A' and number in range(0, 9): 
    frequency = 440
    if number > 4:
        i = 4
        while i != number:
            frequency *= 2
            i += 1
    elif number < 4:
        i = 4
        while i != number:
            frequency /= 2
            i -= 1

elif letter.upper() == 'B' and number in range(0, 9): 
    frequency = 493.88
    if number > 4:
        i = 4
        while i != number:
            frequency *= 2
            i += 1
    elif number < 4:
        i = 4
        while i != number:
            frequency /= 2
            i -= 1

else:
    print('Frequency not present')
print("{:.2f}".format(frequency), 'Hz') 