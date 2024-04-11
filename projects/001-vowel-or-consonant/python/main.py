#--REQUIREMENTS--#
# 1) take use input and save it in a variable
# 2) check if the input is a vowel or yield
# 3) if the input is a vowel, than print that it is a vowel, if it is y than print that
#    it is sometimes a vowel and sometimes a consonant, otherwise print that it is a consonat

letter=input('Please enter a letter:')
vowels='aeiou'
if letter in vowels:
    print('{} is a vowel'.format(letter))
elif letter=='y':
    print('sometimes {a} is a vowel, and sometimes {a} is a consonant'.format(a=letter))
else:
    print('{} is a consonant'.format(letter))