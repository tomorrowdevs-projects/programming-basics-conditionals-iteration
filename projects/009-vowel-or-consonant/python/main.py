user_letter = input('Enter a letter of alphabet:\n')

if user_letter.lower() == 'a' or user_letter.lower() == 'e' or user_letter.lower() == 'i' or user_letter.lower() == 'o' or user_letter.lower() == 'u':
    print('The entered letter is a vowel!')
elif user_letter.lower() == "y":
    print('Sometimes y is a vowel, and sometimes y is a consonant')
else:
    print('The letter is a consonant')

