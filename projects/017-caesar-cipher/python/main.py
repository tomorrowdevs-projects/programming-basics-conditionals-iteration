message=input("Please, enter the message you want to cipher:")
#CHECK FOR CORRECT INPUT#
#Uncomment line 4 and comment lines from 5 to 11 to pass the test (mock input pass an int value so removeprefix rise an error)
# shift=input("Please, enter the shift factor:")
while True:
    shift=input("Please, enter the shift factor:")
    if shift.removeprefix('-').isdecimal():
        shift=int(shift)
        break
    else:
        print("Please, enter a numeric shift (or press ctrl+c to quit):")

new_message=""
for index in range(0,len(message)):
    char=message[index]
    if char.isalpha():
        char=ord(char)
        if 65<=char<=90:
            if char+shift>90:
                char=65+(char+shift-90)-1
            elif char+shift<65:
                char=90+(char+shift-65)+1
            else:
                char=char+shift
        else:
            if char+shift>122:
                char=97+(char+shift-122)-1
            elif char+shift<97:
                char=122+(char+shift-97)+1
            else:
                char=char+shift
        new_message=new_message+chr(char)
    else:
        new_message=new_message+char
print(new_message)