
u_letter = input('Insert a letter: \n')

u_letter = u_letter.lower()

if (u_letter == 'a' or 
    u_letter == 'e' or 
    u_letter == 'i' or 
    u_letter == 'o' or 
    u_letter == 'u'):
    print('The entered letter is a vowel')

elif u_letter == 'y':
    print('sometimes y is a vowel, and sometimes y is a consonant')

elif (u_letter == 'b' or 
      u_letter == 'c' or 
      u_letter == 'd' or 
      u_letter == 'f' or 
      u_letter == 'g' or 
      u_letter == 'h' or 
      u_letter == 'j' or 
      u_letter == 'k' or 
      u_letter == 'l' or 
      u_letter == 'm' or 
      u_letter == 'n' or 
      u_letter == 'p' or 
      u_letter == 'q' or 
      u_letter == 'r' or 
      u_letter == 's' or 
      u_letter == 't' or 
      u_letter == 'v' or 
      u_letter == 'z' or 
      u_letter == 'x' or 
      u_letter == 'y' or 
      u_letter == 'z'):
    print('the entered letter is a consonant')

else:
    print('not a letter')