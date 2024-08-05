
x = 1

while x <= 100:
    if x % 3 == 0 and x % 5 != 0:
        print('fizz')
    
    elif x % 5 == 0 and x % 3 != 0:
        print('buzz')
    
    elif x % 3 == 0 and x % 5 == 0:
        print('fizz buzz')

    else:
        print(x)
        
    x = x + 1

