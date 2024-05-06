counter=0
sum=0
while True:
    number=float(input('Please keep iputing the numbers whose mean you are interested in and input 0 when you have finished:'))
    if counter==1 and number==0:
        print('Please type at least one number before typing 0')
    else:
        if number==0:
            break
        else:
            sum+=number
            counter+=1
mean=round(sum/counter,2)
print('Mean = {}'.format(mean))