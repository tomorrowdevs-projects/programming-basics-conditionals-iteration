#--REQUIREMENTS--#
# 1) take user input and save it to a variable
# 2) wrote the frequencies for the the fourth octave of each note
# 3) calculate and print the frequency fot the note of the user

note=input('Please input the name of the note:')
letter=note[0].lower()
octave=int(note[1])

#frequencies for the fourth octave of each note
if letter=='a':
    frequency=440.00
elif letter=='b':
    frequency=493.88
elif letter=='c':
    frequency=261.63
elif letter=='d':
    frequency=293.66
elif letter=='e':
    frequency=329.23
elif letter=='f':
    frequency=349.23
elif letter=='g':
    frequency=392.00
else:
    print('You have entered a wrong note name, please restart the app and write a right name')
frequency*=(2**(octave-4))
frequency=round(frequency,1)
print(frequency)

