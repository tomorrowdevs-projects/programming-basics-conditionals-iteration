integer=int(input("Enter a positive integer: "))

while integer>0:
    
    while integer!=1:
        if integer%2==0:
            value_sequence=integer//2
            print(value_sequence, end=" ")
        else:
            value_sequence=(integer*3)+1
            print(value_sequence, end=" ")
        integer=value_sequence
    
    integer=int(input("\nEnter a positive integer: "))