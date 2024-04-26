number=int(input('Please, enter the integer you are interested in (integer has to be greater than 2):'))
if number<2:
    print('Plese, enter an integer greater than 2')
else:
    n=2
    flag=1
    while flag<number:
        if number%n==0:
            flag*=n
            print(n)
            n+=1
        else:
            n+=1