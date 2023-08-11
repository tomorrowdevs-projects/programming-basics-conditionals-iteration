def collatz(n):
    sequence = [n]
    while n > 1: 
        if n % 2 == 0: 
            n = n // 2 
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence


while True: 
    n = int(input("Enter a positive integer [0 or less to quit]: "))
    if n <= 0: 
        print("Exiting...")
        break
    else: 
        collatz_sequence = collatz(n)
        print(collatz_sequence)

    