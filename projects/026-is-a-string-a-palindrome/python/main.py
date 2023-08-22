user_string = input('Enter a string:\n')

if user_string == user_string[::-1]:
    print(f'{user_string} is a palindrome!')
else:
    print(f'{user_string} is not a palindrome!')