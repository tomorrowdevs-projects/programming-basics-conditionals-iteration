minutes=int(input('Please, input the number of air minutes of this month:'))
messages=int(input('Please, input the number of messages of this month:'))

if minutes>50:
    extra_min=minutes-50
else:
    extra_min=0

if messages>50:
    extra_mex=messages-50
else:
    extra_mex=0

fee_minutes=round(extra_min*0.25,2)
fee_mex=round(extra_mex*0.15,2)
fee_total=15+fee_minutes+fee_mex+0.44
tax=round(0.05*fee_total,2)
bill=fee_total+tax

if extra_mex==0 and extra_min==0:
    print('Base charge: 15€\n911 fee: 0.44€\nTax: {}€\n\
Total bill amount: {}€'.format(tax,bill))
elif extra_mex==0:
    print('Base charge: 15€\nExtra minutes charge: {}€\n911 fee: 0.44€\nTax: {}€\n\
Total bill amount: {}€'.format(fee_minutes,tax,bill))
elif extra_min==0:
    print('Base charge: 15€\nExtra messages charge: {}€\n911 fee: 0.44€\nTax: {}€\n\
Total bill amount: {}€'.format(fee_mex,tax,bill))
else:
    print('Base charge: 15€\nExtra minutes charge: {}€\nExtra messages charge: {}€\n911 fee: 0.44€\nTax: {}€\n\
Total bill amount: {}€'.format(fee_minutes,fee_mex,tax,bill))