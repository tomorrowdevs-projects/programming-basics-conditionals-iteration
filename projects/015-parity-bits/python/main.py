while True:
    string=input("Please, enter a 8 bit string:")
    if len(string)>8:
        print("You have entered a tring with lenght major than 8 bit. Please, enter a 8 bit string or press ctrl+c to exit.")
    elif string=="":
        break
    else:
        one_bit_number=string.count('1')
        if one_bit_number%2==0:
            print("The parity bit is {}".format(0))
        else:
            print("The parity bit is {}".format(1))