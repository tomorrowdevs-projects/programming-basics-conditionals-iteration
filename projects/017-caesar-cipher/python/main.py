
# user_message = input('Write a message: ').lower()
# user_shift = int(input('supply a shift amount: '))
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for letter in user_message:
#     if letter not in alphabet:
#         print(letter)
    
#     else:
#         position = alphabet.index(letter)
#         new_position = position + user_shift
        
#         if new_position >= len(alphabet):
#             restart = new_position - len(alphabet)
#             cipher = alphabet[restart]
        
#         else:
#             cipher = alphabet[new_position]
        
#     print(cipher)




user_message = input('Write a message: ')
user_shift = int(input('supply a shift amount: '))

for letter in user_message:
    to_number = ord(letter)
    
    if 65 <= to_number <= 90:
        shifted = to_number + user_shift

        if shifted > 90:
            shifted = shifted - 26
            to_letter = chr(shifted)
                    
        else:
            to_letter = chr(shifted)
                    
        print(to_letter)

    elif 97 <= to_number <= 122:
        shifted = to_number + user_shift

        if shifted > 122:
            shifted = shifted - 26
            to_letter = chr(shifted)
                    
        else:
            to_letter = chr(shifted)
            
        print(to_letter)
        
    else:
        print(letter)


