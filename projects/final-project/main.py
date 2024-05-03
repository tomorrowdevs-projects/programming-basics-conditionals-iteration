#---TRIP EXPENSE MANAGER---#

#---Welcome message and note about the currency---#
print('Welcome to the trip expense manager! Please, note that the app doesn\'t use any specific currency, so all expenses have to be\
inserted in the same currency!\n\n')

#---Asking the user for the trip duration---#
while True:
    trip_duration=input('Please, enter the trip duration in days:')
    #Checking user input
    if len(trip_duration)<1:
        print('You have inserted a blanck input, please provide a valid number of days\n\n')
    elif not trip_duration.isdigit():
        print('You have insert a floating point number or a literal input, plese provide a valid number of days\n\n')
    else:
        trip_duration=int(trip_duration)
        break

#---Asking the user for the trip budget---#
while True:
    budget=input('Please, enter the trip budget:')
    #Checking user input
    if len(budget)<1:
        print('You have inserted a blanck input, please provide a valid budget\n\n')
    elif budget.isalpha():
        print('You have inserted a literal input, please provide a valid budget\n\n')
    else:
        budget=float(budget)
        if budget<=0:
            print('You have inserted a null or negative input, please provide a valid budget\n\n')
        else:
            break

#---Initializing the general variables---#
categories=['accomodation','transports','meals','souvenirs','unforseens']
categories_abb=['ACC','TRA','MEA','SOU','UNF']
daily_report=''
TOT_EXP=0 #grand total expense
ACC_EXP=0 #accomodation total expense
TRA_EXP=0 #transport total expense
MEA_EXP=0 #meal total expense
SOU_EXP=0 #souvenir total expense
UNF_EXP=0 #unforseen total expense
for day in range(1,trip_duration+1): #category and total daily expense
    assignment='D{}_TOT_EXP=0'.format(day)
    exec(assignment)
    for category in categories_abb:
        assignment='D{}_{}_EXP=0'.format(day,category)
        exec(assignment)

#---Asking the user for expense---#
for day in range(1,trip_duration+1):
    daily_report='{}DAY {}\n'.format(daily_report,day)
    for i in range(0,len(categories)):
        while True: #Asking accomodation expense
            expense=input('Please, enter the {} expense for day {}:'.format(categories[i],day))
            if len(expense)<1:
                print('You have inserted a blanck input, please provide a valid expense\n\n')
            elif expense.isalpha():
                print('You have inserted literal input, please provide a valid expense\n\n')
            else:
                expense=float(expense)
                if expense<0:
                    print('You have inserted a negative input, please provide a valid expense\n\n')
                else:
                    break
        assignment='D{}_{}_EXP={:.2f}'.format(day,categories_abb[i],expense)
        exec(assignment)
        daily_report='{}Expense for {}:{:.2f}\n'.format(daily_report,categories[i],expense)
        assignment='D{D}_TOT_EXP+=D{D}_{C}_EXP'.format(D=day,C=categories_abb[i])
        exec(assignment)
    daily_report='{}Total expense for the day:{:.2f}\n\n'.format(daily_report,eval('D{}_TOT_EXP'.format(day)))
#---Performing changes on charges or print report---#
while True:
    while True: #Asking the user what he wants to do
        print('This is the list of the daily expenses that you inserted:')
        print(daily_report) #printing the expense list
        operation=input('\nChoose the number relevant to the operation you want to perform: modify expense [1],\
report [2]:')
        if len(operation)<1:
            print('You have inserted a blanck input, please provide a valid number of operation\n\n')
        elif not operation.isdigit():
            print('You have insert a floating point number or a literal input, plese provide a valid number of operation\n\n')
        else:
            operation=int(operation)
            if not operation in range(1,3):
                print('You have entered a not existing number of operation, please enter a valid number of operation\n\n')
            else:
                break
    if operation==1:
        while True: #Asking the user for the day to be modified
            day=input('Take a look to the list of the expenses you have inserted and choose the day you want to modify:')
            if len(day)<1:
                print('You have inserted a blanck input, please provide a valid day numbert\n\n')
            elif not day.isdigit():
                print('You have insert a floating point number or a literal input, plese provide a valid day number\n\n')
            else:
                day=int(day)
                if day>trip_duration:
                    print('You have exceeded the duration of the trip, please enter a valid day number\n\n')
                else:
                    break
        
        while True: #Asking the user for the category to be modified
            index=input('Take a look to the list of the expenses you have inserted and choose the number relevant to the category\
you want to modify: accomodation [1], transports [2], meals [3], souvenirs [4], unforseens [5]')
            if len(index)<1:
                print('You have inserted a blanck input, please provide a valid integer\n\n')
            elif not index.isdigit():
                print('You have insert a floating point number or a literal input, plese provide a valid integer\n\n')
            else:
                index=int(index)-1
                if index in range(0,5):    
                    break
                else:
                    print('The number doesn\'t match with any category, please enter a valid integer\n\n')

        #Asking the user for the new expense value
        while True:
            expense=input('Please, enter the new expense:')
            if len(expense)<1:
                print('You have inserted a blanck input, please provide a valid expense\n\n')
            elif expense.isalpha():
                print('You have inserted literal input, please provide a valid expense\n\n')
            else:
                expense=float(expense)
                if expense<0:
                    print('You have inserted a negative input, please provide a valid expense\n\n')
                else:
                    break

        #Updating the daily totals with new expense value
        assignment='D{D}_TOT_EXP-=D{D}_{C}_EXP'.format(D=day,C=categories_abb[index])
        exec(assignment)
        assignment='D{}_{}_EXP={:.2f}'.format(day,categories_abb[index],expense)
        exec(assignment)
        assignment='D{}_TOT_EXP+={:.2f}'.format(day,expense)
        exec(assignment)
        for day in range(1,trip_duration+1):
            daily_report='{}DAY {}\n'.format(daily_report,day)
            for i in range(0,len(categories)):
                daily_report='{}Expense for {}:{:.2f}\n'.format(daily_report,categories[i],eval('D{}_{}_EXP'.format(day,categories_abb[i])))
            daily_report='{}Total expense for the day:{:.2f}\n\n'.format(daily_report,eval('D{}_TOT_EXP'.format(day)))
    elif operation==2:
        for day in range(1,trip_duration+1):
            for category in categories_abb:
                assignment='{C}_EXP+=D{D}_{C}_EXP'.format(C=category,D=day)
                exec(assignment)
        for category in categories_abb:
            assignment='TOT_EXP+={}_EXP'.format(category)
            exec(assignment)

        trip_balance=budget-TOT_EXP
        if trip_balance<0:
            balance_mex='You exceeded the trip budget of {:.2f}'.format(abs(trip_balance))
        elif trip_balance>0:
            balance_mex='You saved {:.2f}'.format(trip_balance)
        else:
            balance_mex='You spent the whole trip budget'
        report='Here the report of your trip:\n\
TOTAL EXPENSE: {:.2f}\n\
ACCOMODATION EXPENSE: {:.2f}\n\
TRANSPORT EXEPENSE: {:.2f}\n\
MEAL EXPENSE: {:.2f}\n\
SOUVENIRS EXPENSE: {:.2f}\n\
UNFORSEENS EXPENSE: {:.2f}\n\
\n\
{}'.format(TOT_EXP,ACC_EXP,TRA_EXP,MEA_EXP,SOU_EXP,UNF_EXP,balance_mex)
        print(report)
        break