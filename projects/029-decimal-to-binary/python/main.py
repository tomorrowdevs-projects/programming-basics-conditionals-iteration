def dec_to_bin(n):
    result = ""
    while n > 0:
        n_remainder = n % 2
        n_remainder = str(n_remainder)
        result += n_remainder
        n = n // 2
    return result[::-1]

n = int(input("Enter an integer: "))
result = dec_to_bin(n)
print(f'Binary conversion of {n}: {result}')