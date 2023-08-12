def prime_factors(n):
    factors = []
    factor = 2
    while factor <= n:
        if n % factor == 0: 
            factors.append(factor)
            n = n // factor 
        else:
            factor = factor + 1
    return factors


n = int(input("Please enter a positive integer, equal or greater than 2: "))

if n < 2: 
        print("Error. Integer must be equal or greater than 2.")
else:   
    factors = prime_factors(n)
    print(f'Prime factors of {n} are:')
    for factor in factors:
        print(factor)  
    

        