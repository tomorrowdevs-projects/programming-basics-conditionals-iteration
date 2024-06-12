
u_note = input('Insert a note: ')
u_note = u_note.upper()
x = int(u_note[1])

if u_note[0] == 'C':
    freq = 261.63 / (2**(4-x))
    print(f'{freq:.2f}')

elif u_note[0] == 'D':
    freq = 293.66 / (2**(4-x))
    print(f'{freq:.2f}')

elif u_note[0] == 'E':
    freq = 329.63 / (2**(4-x))
    print(f'{freq:.2f}')

elif u_note[0] == 'F':
    freq = 349.23 / (2**(4-x))
    print(f'{freq:.2f}')

elif u_note[0] == 'G':
    freq = 392.00 / (2**(4-x))
    print(f'{freq:.2f}')

elif u_note[0] == 'A':
    freq = 440.00 / (2**(4-x))
    print(f'{freq:.2f}')

elif u_note[0] == 'B':
    freq = 493.88 / (2**(4-x))
    print(f'{freq:.2f}')

else :
    print('Not a note')

