import random
spin=random.randint(0,37)

if spin==0:
    print("Pay 0")
elif spin==37:
    print("Pay 00")
else:
    if spin<11:
        if spin%2==0:
            print(f"Pay {spin}")
            print("Pay Black")
            print("Pay Even")
            print("Pay 1 to 18")
        else:
            print(f"Pay {spin}")
            print("Pay Red")
            print("Pay Odd")
            print("Pay 1 to 18")
    
    elif spin>10 and spin<19:
        if spin%2==0:
            print(f"Pay {spin}")
            print("Pay Red")
            print("Pay Even")
            print("Pay 1 to 18")
        else:
            print(f"Pay {spin}")
            print("Pay Black")
            print("Pay Odd")
            print("Pay 1 to 18")
            
    elif spin>18 and spin<29:
        if spin%2==0:
            print(f"Pay {spin}")
            print("Pay Black")
            print("Pay Even")
            print("Pay 19 to 36")
        else:
            print(f"Pay {spin}")
            print("Pay Red")
            print("Pay Odd")
            print("Pay 19 to 36")
    else:
        if spin%2==0:
            print(f"Pay {spin}")
            print("Pay Red")
            print("Pay Even")
            print("Pay 19 to 36")
        else:
            print(f"Pay {spin}")
            print("Pay Black")
            print("Pay Odd")
            print("Pay 19 to 36")