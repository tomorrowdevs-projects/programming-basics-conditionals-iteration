q = int(input('Enter decimal number:\n'))
result = ''

while q != 0:
    r = q % 2
    result = str(r) + result
    q = q // 2
print(f'The binary number corresponding is: {result}')
