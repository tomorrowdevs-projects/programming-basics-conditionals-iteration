factor = 2
u_integer = int(input('Enter an integer (2 or greater): '))

if u_integer < 2:
    print('Integer must be >= 2')

else:
    while factor <= u_integer:
        if u_integer % factor == 0:
            u_integer = u_integer // factor
            print(factor)
        
        else:
            factor += 1
