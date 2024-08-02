# byte =[]
# x = 0
# u_bit = 'none'

# while u_bit != '':
#     x = x + 1
#     u_bit = input(f'Insert the bit number {x}: ')
#     byte.append(u_bit)
       

# if x == 9 and u_bit == '':
#     n = byte.count('1')
#     if n % 2 == 0:
#         print('The parity bit is: 0')
    
#     else:
#         print('The parity bit is: 1')

# else:
#     print('The number of bits must be equal to 8')
    




byte = []
x = 0
u_bit = 'none'

while x < 8 and u_bit != '':
    x = x + 1
    u_bit = input(f'Insert the bit number {x}: ')
    byte.append(u_bit)
    
    
if x <= 8 and u_bit == '':
    print('The number of bits must be equal to 8')

else:
    n = byte.count('1')
    
    if n % 2 == 0:
        print('The parity bit is: 0')
        
    else:
        print('The parity bit is: 1')
