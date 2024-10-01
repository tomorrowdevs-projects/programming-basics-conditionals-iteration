string=input("Enter a string of 8 bits: ")

while string!="":
    if len(string)==8:
        one_bit_number=string.count("1")
        if one_bit_number%2==0:
            print("The parity bit is 0")
        else:
            print("The parity bit is 1")
            
    else:
        print("You have entered something other than 8 bits")
        
    string=input("Enter a string of 8 bits: ")