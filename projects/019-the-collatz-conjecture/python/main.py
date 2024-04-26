while True:
    number=int(input('Please enter a positive integer as first element of the sequence or enter 0 or a negative integer to quit:'))
    sequence=''
    if number<=0:
        break
    else:
        while number>1:
            print(number)
            if number%2==0:
                number=number//2
            else:
                number=number*3+1
        print(1)

