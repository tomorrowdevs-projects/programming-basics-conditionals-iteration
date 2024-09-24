user_word = input('Insert a word: ')

letters_counter = len(user_word)
half_word = letters_counter//2
reverse_counter = letters_counter - 1
counter = 0
is_palindrome = False

while counter < half_word:
    if user_word[counter] == user_word[reverse_counter]:
        counter += 1
        reverse_counter -= 1
        is_palindrome = True
        
    else:
        break
    
if not is_palindrome:
    print(f'{user_word} is not palindrome')

else:
    print (f'{user_word} is palindrome')
