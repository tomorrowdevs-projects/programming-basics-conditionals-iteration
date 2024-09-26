sequence = 1

while sequence > 0:
    sequence = int(input('insert an integer: '))

    while sequence > 1:
        is_even = sequence % 2
        
        if is_even == 0:
            sequence = sequence // 2
            print(sequence)
    
        else:
            sequence = sequence * 3 + 1
            print(sequence)



