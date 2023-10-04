message = input('insert a message to encode or decode: ')
number = int(input('insert a positive number to encode or negative to decode: '))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_message = ''
numbers = '0123456789'

for i in message:
    if i in numbers or i == ' ':
        new_message += i
    elif i == 'à':
        i = 'a'
    elif i == 'è' or i == 'é':
        i = 'e'
    elif i == 'ì':
        i = 'i'
    elif i == 'ò':
        i = 'o'
    elif i == 'ù':
        i = 'u'
    for e in alphabet:
        if e == i:
            index = alphabet.index(e)
            if index + number >= 26:
                new_message += alphabet [(index + (number)) % 26]
            else: 
                new_message += alphabet[index + (number)]
print(new_message)