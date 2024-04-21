while True:
    x0=input('Please enter the x coordinate for the first point of the polygon:')
    if not x0.isnumeric():
        print('Please, enter a numeric value or presse ctrl+c to quit the app')
    else:
        x0=int(x0)
        break

while True:
    y0=input('Please enter the y coordinate for the first point of the polygon:')
    if not y0.isnumeric():
        print('Please, enter a numeric value or presse ctrl+c to quit the app')
    else:
        y0=int(y0)
        break

perimiter=0
exit_flag=True
while exit_flag:
    x=input('Please enter the x coordinate for the next point of the polygon (blanck to quit the app):')
    if len(x)>0:
        x=int(x)
        while True:
            y=input('Please enter the y coordinate for the next point of the polygon:')
            if not y.isnumeric():
                print('Please, enter a numeric value or presse ctrl+c to quit the app')
            else:
                y=int(y)
                break
        perimiter+=((x0-x)**2+(y0-y)**2)**0.5
        x0=x
        y0=y
    else:
        exit_flag=False

print('The perimiter of that polygon is {}'.format(round(perimiter,2)))