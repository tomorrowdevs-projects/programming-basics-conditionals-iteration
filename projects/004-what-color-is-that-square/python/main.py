position=input('Please, insert the cell position on the chess board:')
column=position[0]
row=int(position[1])
if (column in 'aceg'):
    if row%2>0:
        print('Cell color is black')
    else:
        print('Cell color is white')
else:
    if row%2>0:
        print('Cell color is white')
    else:
        print('Cell color is black')