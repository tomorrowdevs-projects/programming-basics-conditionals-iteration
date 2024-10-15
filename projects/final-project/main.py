#Travel Expense Manager

#Ask the user for the number of travel days and the total budget available.
travel_days=int(input("Enter the number of travel days: "))
available_budget=float(input("Enter the total budget available for the trip: "))

#Using a for loop, ask the user to enter daily expenses for different categories.
#Use the assignment operator (+=) to accumulate daily expenses into total variables for each category.
#Use a while loop to allow the user to correct any expense entry errors.
lodging_expenses=0
transport_expenses=0
meals_expenses=0
attractions_expenses=0

for i in range(travel_days):
    is_valid_input=False
    while not(is_valid_input):
        lodging=input("Enter daily expenses for lodging: ")
        replaced_input=lodging.replace(".","")
        if replaced_input.isnumeric():
            lodging=float(lodging)
            is_valid_input=True
        else:
            print("Invalid input")
    lodging_expenses+=lodging

    is_valid_input=False
    while not(is_valid_input):
        transport=input("Enter daily expenses for transport: ")
        replaced_input=transport.replace(".","")
        if replaced_input.isnumeric():
            transport=float(transport)
            is_valid_input=True
        else:
            print("Invalid input")
    transport_expenses+=transport   

    is_valid_input=False
    while not(is_valid_input):
        meals=input("Enter daily expenses for meals: ")
        replaced_input=meals.replace(".","")
        if replaced_input.isnumeric():
            meals=float(meals)
            is_valid_input=True
        else:
            print("Invalid input")
    meals_expenses+=meals  

    is_valid_input=False
    while not(is_valid_input):
        attractions=input("Enter daily expenses for attractions: ")
        replaced_input=attractions.replace(".","")
        if replaced_input.isnumeric():
            attractions=float(attractions)
            is_valid_input=True
        else:
            print("Invalid input")
    attractions_expenses+=attractions 

#Calculate the total expense.
#Print to screen a summary of total expenses for each category and the grand total of expenses.

total_expense=lodging_expenses+transport_expenses+meals_expenses+attractions_expenses

print(f"Lodging expenses: {lodging_expenses:.2f} $")
print(f"Transport expenses: {transport_expenses:.2f} $")
print(f"Meals expenses: {meals_expenses:.2f} $")
print(f"Attractions expenses: {attractions_expenses:.2f} $")
print(f"Total expense: {total_expense:.2f} $")

#Ask the user if they want to make changes to the charges and allow editing of previous charges.
#Automatically update expense totals based on user changes.
#I used a while loop to allow the user to correct any changes entry errors.

is_valid_input=False
while not(is_valid_input):
    ask_change=input("Do you want to make a change? (Enter yes/no): ")
    if ask_change=="yes" or ask_change=="no":
        is_valid_input=True
    else:
        print("Invalid input")

if ask_change=="yes":
    is_valid_category=False
    while not(is_valid_category):
        ask_category=input("Enter a category (lodging/transport/meals/attractions): ")
        if ask_category=="lodging" or ask_category=="transport" or ask_category=="meals" or ask_category=="attractions":
            is_valid_category=True
        else:
            print("Invalid category")

    if ask_category=="lodging":
        is_valid_change=False
        while not(is_valid_change):
            lodging=input("Enter change for the lodging expenses: ")
            replaced_input=lodging.replace(".","")
            if replaced_input.isnumeric():
                lodging=float(lodging)
                lodging_expenses=lodging
                is_valid_change=True
            else:
                print("Invalid change")

    elif ask_category=="transport":
        is_valid_change=False
        while not(is_valid_change):
            transport=input("Enter change for the transport expenses: ")
            replaced_input=transport.replace(".","")
            if replaced_input.isnumeric():
                transport=float(transport)
                transport_expenses=transport
                is_valid_change=True
            else:
                print("Invalid change")

    elif ask_category=="meals":
        is_valid_change=False
        while not(is_valid_change):
            meals=input("Enter change for the meals expenses: ")
            replaced_input=meals.replace(".","")
            if replaced_input.isnumeric():
                meals=float(meals)
                meals_expenses=meals
                is_valid_change=True
            else:
                print("Invalid change")

    elif ask_category=="attractions":
        is_valid_change=False
        while not(is_valid_change):
            attractions=input("Enter change for the attractions expenses: ")
            replaced_input=attractions.replace(".","")
            if replaced_input.isnumeric():
                attractions=float(attractions)
                attractions_expenses=attractions
                is_valid_change=True
            else:
                print("Invalid change")

    total_expense=lodging_expenses+transport_expenses+meals_expenses+attractions_expenses    
    print(f"Updated total expense: {total_expense:.2f} $")

#Show if the available budget has been respected or expenses have been exceeded.
if total_expense>available_budget:
    print("You have exceeded your budget!")
else:
    print("You respected the available budget!")
