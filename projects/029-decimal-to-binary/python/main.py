# set a variable where store result as an empty string
result = ''

# ask to user a decimal number to convert 
q = int(input('Type a number to convert in binary: '))

# perform the computation and print the result
while q != 0:
    r = q % 2
    result += str(r)
    q = q // 2
print(f'The binary value of the number is : {result}')