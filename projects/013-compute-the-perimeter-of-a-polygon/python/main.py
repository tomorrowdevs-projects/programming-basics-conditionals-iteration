while True:
    x0=input('Please enter the x coordinate for the first point of the polygon:')
    if x0.count('.')>1 and not x0.lstrip('.').isdecimal():
        print('Please, enter a numeric value or presse ctrl+c to quit the app')
    else:
        x0=float(x0)
        break

while True:
    y0=input('Please enter the y coordinate for the first point of the polygon:')
    if y0.count('.')>1 and not y0.lstrip('.').isdecimal():
        print('Please, enter a numeric value or presse ctrl+c to quit the app')
    else:
        y0=float(y0)
        break

perimiter=0
while True:
    x=input('Please enter the x coordinate for the next point of the polygon (blanck to quit the app):')
    if len(x)>0:
        if x.count('.')>1 and not x.lstrip('.').isdecimal():
            print('Please, enter a numeric value or presse ctrl+c to quit the app')
            continue
        else:
            x=float(x)

        while True:
            y=input('Please enter the y coordinate for the next point of the polygon:')
            if y.count('.')>1 and not y.lstrip('.').isdecimal():
                print('Please, enter a numeric value or presse ctrl+c to quit the app')
            else:
                y=float(y)
                break
        perimiter+=((x0-x)**2+(y0-y)**2)**0.5
        x0=x
        y0=y
    else:
        break

print('The perimiter of that polygon is {}'.format(round(perimiter,2)))