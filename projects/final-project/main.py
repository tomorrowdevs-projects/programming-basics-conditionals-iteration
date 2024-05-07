#---TRIP EXPENSE MANAGER---#

#---Welcome message and note about the currency---#
print("""Welcome to the trip expense manager! Please, note that the app doesn't use any specific currency, so all expenses have to be inserted in the same currency!\n\n""")

#---Asking the user for the trip duration---#
trip_duration=input('Please, enter the trip duration in days:')
while not trip_duration.isdecimal():
    trip_duration=input('Please, provide a valid trip duration in days:')
trip_duration=int(trip_duration)

#---Asking the user for the trip budget---#
budget=input('Please, enter the trip budget:')
while budget.count('.')>1 or not budget.strip('.').isdecimal():
    budget=input('Please, provide a valid trip budget:')
budget=float(budget)

#---Initializing the general variables---#
grd_tot_exp=0 #grand total expense
acc_tot_exp=0 #accomodation total expense
tra_tot_exp=0 #transport total expense
mea_tot_exp=0 #meal total expense
sou_tot_exp=0 #souvenir total expense
unf_tot_exp=0 #unforseen total expense
acc_exp=list() #daily accomodation expense list
tra_exp=list() #daily transport expense list
mea_exp=list() #daily meal expense list
sou_exp=list() #daily souvenir expense list
unf_exp=list() #daily unforseen expense list

#---Asking the user for expense---#
for day in range(1,trip_duration+1):
    #Accomodation expense
    expense=input('Please, enter the accomodation expense for day {}:'.format(day))
    while expense.count('.')>1 or not expense.strip('.').isdecimal():
        expense=input('Please, enter a valid accomodation expense for day {}:'.format(day))
    expense=round(float(expense),2)
    acc_exp.append(expense)

    #Transports expense
    expense=input('Please, enter the transports expense for day {}:'.format(day))
    while expense.count('.')>1 or not expense.strip('.').isdecimal():
        expense=input('Please, enter a valid transports expense for day {}:'.format(day))
    expense=round(float(expense),2)
    tra_exp.append(expense)

    #Meals expense
    expense=input('Please, enter the meals expense for day {}:'.format(day))
    while expense.count('.')>1 or not expense.strip('.').isdecimal():
        expense=input('Please, enter a valid meals expense for day {}:'.format(day))
    expense=round(float(expense),2)
    mea_exp.append(expense)

    #Souvenirs expense
    expense=input('Please, enter the souvenirs expense for day {}:'.format(day))
    while expense.count('.')>1 or not expense.strip('.').isdecimal():
        expense=input('Please, enter a valid souvenirs expense for day {}:'.format(day))
    expense=round(float(expense),2)
    sou_exp.append(expense)

    #Unforseens expense
    expense=input('Please, enter the unforseens expense for day {}:'.format(day))
    while expense.count('.')>1 or not expense.strip('.').isdecimal():
        expense=input('Please, enter a valid unforseens expense for day {}:'.format(day))
    expense=round(float(expense),2)
    unf_exp.append(expense)

#---Building the daily report---#
daily_report='Accomodation: {}\nTransports: {}\nMeals: {}\nSouvenirs: {}\nUnforseens: {}\n\n'.format(acc_exp,tra_exp,mea_exp,sou_exp,unf_exp)

#---Performing changes on charges or printing report---#
#Showing user the previous inputs
operation=1
while operation==1:
    #Showing user the previous inputs
    print('This is the list of the daily expenses that you inserted (note that each list element is sorted by day):')
    print(daily_report)

    #Asking user for the operation to perform
    operation=input('Choose the number relevant to the operation you want to perform: modify expense [1], report [2]:')
    while not (operation=='1' or operation=='2'):
        operation=input('Please, provide a valid number of operation:')
    operation=int(operation)

    #Performing the chosen operation
    if operation==1:
        #Asking user for the day to be modified
        days=list(range(1,trip_duration+1))
        days=list(map(str,days))
        day=input('Take a look to the list of the expenses you have inserted and choose the day you want to modify:')
        while not day in days:
            day=input('Please, provide a valid number of day:')
        day=int(day)

        #Asking the user for the category to be modified
        category=input('Take a look to the list of the expenses you have inserted and choose the number relevant to the category you want to modify: accomodation [1], transports [2], meals [3], souvenirs [4], unforseens [5]')
        while not category in ['1','2','3','4','5']:
            category=input('Please, provide a valid number of category:')
        category=int(category)

        #Asking the user for the new expense value
        expense=input('Please, enter the new expense amount:')
        while expense.count('.')>1 or not expense.strip('.').isdecimal():
            expense=input('Please, enter a valid expense amount')
        expense=round(float(expense),2)

        #Performing the expense substitution
        if category==1:
            acc_exp[day-1]=expense
        elif category==2:
            tra_exp[day-1]=expense
        elif category==3:
            mea_exp[day-1]=expense
        elif category==4:
            sou_exp[day-1]=expense
        else:
            unf_exp[day-1]=expense

        #---Updating the daily report---#
        daily_report='Accomodation: {}\nTransports: {}\nMeals: {}\nSouvenirs: {}\nUnforseens: {}\n\n'.format(acc_exp,tra_exp,mea_exp,sou_exp,unf_exp)
    else:
        #Daily totals calculation
        for index in range(trip_duration):
            acc_tot_exp+=acc_exp[index]
            tra_tot_exp+=tra_exp[index]
            mea_tot_exp+=mea_exp[index]
            sou_tot_exp+=sou_exp[index]
            unf_tot_exp+=unf_exp[index]
        grd_tot_exp=acc_tot_exp+tra_tot_exp+mea_tot_exp+sou_tot_exp+unf_tot_exp

        #Checking trip balance
        trip_balance=budget-grd_tot_exp
        if trip_balance<0:
            balance_mex='You exceeded the trip budget of {:.2f}'.format(abs(trip_balance))
        elif trip_balance>0:
            balance_mex='You saved {:.2f}'.format(trip_balance)
        else:
            balance_mex='You spent the whole trip budget'

        #Printing report
        print('Here is the report of your trip:')
        print('TOTAL EXPENSE: {:.2f}\nACCOMODATION EXPENSE: {:.2f}'.format(grd_tot_exp,acc_tot_exp))
        print('TRANSPORT EXEPENSE: {:.2f}\nMEAL EXPENSE: {:.2f}'.format(tra_tot_exp,mea_tot_exp))
        print('SOUVENIRS EXPENSE: {:.2f}\nUNFORSEENS EXPENSE: {:.2f}'.format(sou_tot_exp,unf_tot_exp))
        print(balance_mex)
        break