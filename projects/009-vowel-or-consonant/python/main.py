# ask to user a letter, store in a variable and make it lowercase
letter = input('Type a letter: ').lower()

vowels = 'aeiouàèéìòù'

# compare the given letter to define if it is a vowel or a consonant and print result on screen
if len(letter) > 1 or not letter.isalpha():
    result = 'Not a valid input'
elif letter in vowels:
    result = f'" {letter.upper()} " is a vowel'
elif letter == 'y':
    result = 'sometimes y is a vowel and sometimes y is a consonant'    
else:
    result = f'" {letter.upper()} " is a consonant'

print(result)
