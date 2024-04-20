from random import choice
red=['1','3','5','7','9','12','14','16','18','19','21','23','25','27','30','32','34','36']
green='0-00'
number=choice(['0','00','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36'])
if number=='0' or number=='00':
    output='The spin resulted in {} . . .\nPay {}\n'.format(number,number)
else:
    number=int(number)
    output='The spin resulted in {} . . .\nPay {}\n'.format(number,number)
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