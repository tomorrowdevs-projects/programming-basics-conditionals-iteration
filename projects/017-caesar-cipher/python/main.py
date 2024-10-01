message=input("Enter a message: ")
shift_amount=int(input("Enter the shift amount: "))

for char in message:

    if char.islower()==True and char in "abcdefghijklmnopqrstuvwxyz":
        numeric_code=ord(char)
        shifted_letter=chr((numeric_code-97+shift_amount)%26+97)
        print(shifted_letter, end='')
        
    elif char.islower()==False and char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        numeric_code=ord(char)
        shifted_letter=chr((numeric_code-65+shift_amount)%26+65)
        print(shifted_letter, end='')
        
    else:
        print(char, end="")