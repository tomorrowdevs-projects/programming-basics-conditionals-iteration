
u_selection = input('Insert a chess board position:\n')
u_selection = u_selection.lower()
x = int(u_selection[1])

if (u_selection[0] == 'a' or                                 # on those columns even numbers are WHITE, odd numbers are BLACK 
    u_selection[0] == 'c' or
    u_selection[0] == 'e' or
    u_selection[0] == 'g' 
    ):
    if x % 2 == 0:                                           # control if even
        print('White')
    else:
        print('Black')

elif (u_selection[0] == 'b' or                               # on those columns even numbers are BLACK, odd numbers are WHITE
      u_selection[0] == 'd' or
      u_selection[0] == 'f' or
      u_selection[0] == 'h'
    ):
    if x % 2 == 0:                                           # control if even
        print('Black')
    else:
        print('White')

else:
    print('none')