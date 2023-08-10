# ask to user a integer
number = int(input('Type an integer: '))
factor = 2
result = ''
integer = number

# if statement that check if integer typed is greater or equal than 2, if so ends the computation, otherwise go on with prime factorization and print results using a while cycle
if number < 2:
    result = 'number must be grater or, at least, equal to 2'
    print(result)
else:
    print(f'The prime factor of {integer} are:')
    while number >= factor:
        if number % factor == 0:
            number = number // factor
            print(f'{factor}')
        else:
            factor += 1


