integer=int(input("Enter an integer (2 or greater): "))

if integer>1:
    factor=2
    while factor<=integer:
        if integer%factor==0:
            print(factor)
            integer//=factor
        else:
            factor+=1
else:
    print("The value entered is less than 2")