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
    




# byte = []
# x = 0
# u_bit = None

# while x < 8 and u_bit != '':
#     x = x + 1
#     u_bit = input(f'Insert the bit number {x}: ')
#     byte.append(u_bit)
    
    
# if x <= 8 and u_bit == '':
#     print('The number of bits must be equal to 8')

# else:
#     n = byte.count('1')
    
#     if n % 2 == 0:
#         print('The parity bit is: 0')
        
#     else:
#         print('The parity bit is: 1')


byte = []
counter = 0
is_error = False

for x in range(8):
    u_bit = input(f'Insert the bit number {x}: ')
    if u_bit == '':
        print('The number of bits must be equal to 8')
        is_error = True
        break

    elif u_bit == '1':
        counter += 1
    
    byte.append(u_bit)

if not is_error:
    if counter % 2 == 0:
        print('The parity bit is: 0')
        
    else:
        print('The parity bit is: 1')



