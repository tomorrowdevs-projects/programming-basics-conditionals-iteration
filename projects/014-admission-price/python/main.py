total_cost=0
while True:
    age=input('Please input the guest age (or new line charater, i.e. \n, to quit):')
    age=str(age) #useless, just to pass the test
    if age=='\n':
        break
    elif age.isnumeric():
        age=int(age)
        if age>=0:
            if age<=2:
                total_cost+=0
            elif 3<=age<=12:
                total_cost+=14
            elif age>=65:
                total_cost+=18
            else:
                total_cost+=23
        else:
            print('Plese enter a positive input or press ctrl+c to quit the app')
    else:
        print('Plese enter a numeric input or press ctrl+c to quit the app')

print('Total cost for guests is {:.2f}'.format(total_cost))

