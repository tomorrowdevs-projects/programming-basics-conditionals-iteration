
total = []
u_age = input('Insert guest age: ')

while u_age != '':
    u_age = int(u_age)
    
    if u_age >= 65:
        total.append(18)
    
    elif u_age >= 3 and u_age <= 12:
        total.append(14)
    
    elif u_age <= 2:
        total.append(0)
        
    else:
        total.append(23) 
    
    u_age = input('Insert guest age: ')


print(f'The total cost of the group is: ${sum(total):.2f}')

