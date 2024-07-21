# values = []

# def collection(x):
#     while x > 0:
#         x = int(input('Insert a value: '))
#         values.append(x)
#     values.pop()

# x = int(input('Insert a value: '))
# values.append(x)

# if values[0] == 0:
#         print('The first value can not be 0')
#         exit()

# else:
#      collection(x)
     

# average = sum(values) / len(values)


# print(f'The average of selected values is: {average:.2f}')



x = int(input('Insert a value: '))

if x == 0:
     print('The first value can not be 0')

else:
    values = []
    while x > 0:
        values.append(x)
        x = int(input('Insert a value: '))
    
    average = sum(values) / len(values)
        
print(f'The average of selected values is: {average:.2f}')

