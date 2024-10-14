result = ''
q = int(input('Enter a decimal number: '))
decimal = q

while q > 0:
    r = str(q % 2)
    result = r + result
    q = q // 2

print(f'The binary number of {decimal} is: {result}')