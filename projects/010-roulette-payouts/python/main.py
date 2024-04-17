from random import random
red='1-3-5-7-9-12-14-16-18-19-21-23-25-27-30-32-34-36'
green='0-00'
number=int(random()*37)
if number<1:
    padding=int(random()*2+1)
    number='{:0{pad}d}'.format(number,pad=padding)
    output='The spin resulted in {}...\nPay {}\n'.format(number,number)
else:
    output='The spin resulted in {}...\nPay {}\n'.format(number,number)
    if str(number) in red:
        output=output+'Pay {}\n'.format('Red')
    else:
        output=output+'Pay {}\n'.format('Black')

    if number%2>0:
        output=output+'Pay {}\n'.format('Odd')
    else:
        output=output+'Pay {}\n'.format('Even')

    if 1<=number<=18:
        output=output+'Pay 1 to 18\n'
    else:
        output=output+'Pay 19 to 36\n'

print(output)