letter=input("Enter the letter of the note:")
octave=int(input("Enter the octave of the note:"))

if letter=="C":
   frequency=261.63/2**(4-octave)
   print(f"C{octave} = {frequency:.2f} Hz")

elif letter=="D":
   frequency=293.66/2**(4-octave)
   print(f"D{octave} = {frequency:.2f} Hz")

elif letter=="E":
   frequency=329.63/2**(4-octave)
   print(f"E{octave} = {frequency:.2f} Hz")

elif letter=="F":
   frequency=349.23/2**(4-octave)
   print(f"F{octave} = {frequency:.2f} Hz")

elif letter=="G":
   frequency=392.00/2**(4-octave)
   print(f"G{octave} = {frequency:.2f} Hz")

elif letter=="A":
   frequency=440.00/2**(4-octave)
   print(f"A{octave} = {frequency:.2f} Hz")

elif letter=="B":
   frequency=493.88/2**(4-octave)
   print(f"B{octave} = {frequency:.2f} Hz")

else:
   print("You have entered a wrong note name!")