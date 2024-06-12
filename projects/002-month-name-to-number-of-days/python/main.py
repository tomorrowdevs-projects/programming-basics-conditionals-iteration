
u_month = input('Insert a month: ')

u_month = u_month.lower()

if (u_month == 'jenuary' or
    u_month == 'march' or
    u_month == 'may' or
    u_month == 'july' or
    u_month == 'august' or
    u_month == 'october' or
    u_month == 'december'):
    print('31')

elif u_month == 'february':
    print('28 or 29')

elif (u_month == 'april' or
      u_month == 'june' or
      u_month == 'september' or
      u_month == 'november'):
    print('30')

else :
    print('Not a month')