number=input('Please, insert a positive integer:')
q=int(number)
result=''
while q>0:
    r=q%2
    result=str(r)+result
    q=q//2
print('You have insert {}, which is equal to {} in binary notation'.format(number,result))