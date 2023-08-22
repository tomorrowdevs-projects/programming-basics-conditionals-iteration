import string

user_message = input('Enter your message:\n').lower()
letter_shift = int(input('Enter the amount of shift:\n'))
new_message = []
for letter in user_message:
    if letter in string.ascii_lowercase:
        i = (string.ascii_lowercase.index(letter) + letter_shift) % 26
        new_message.append(string.ascii_lowercase[i])
    else:
        new_message.append(letter)

print("".join(new_message))