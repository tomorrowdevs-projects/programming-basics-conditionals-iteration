user_input = input('type a word: ')

new_word = ''

for i in reversed(user_input):
    new_word += i

if new_word == user_input:
    result = f'{user_input} is a palindrome'
else:
    result = f'{user_input} is not a palindrome'

print(result)