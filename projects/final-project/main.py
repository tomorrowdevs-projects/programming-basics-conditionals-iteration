'''
Main features
Acquisition of travel information:

Ask the user for the number of travel days and store it in a numeric variable.
Ask the user for the total budget available for the trip and store it in a numeric variable.
'''

travel_days = int(input('Enter the total days for the trip:\n'))
total_budget = int(input('Enter the total budget available in $ for the trip:\n'))
print(f"Great! Your trip will last {travel_days} days with an initial budget of ${total_budget}")

total_expenses = 0
total_meal_expenses = 0
total_transport_expenses = 0
total_accommodation_expenses = 0

i = 1

'''
Registration of daily expenses
Using a for loop, ask the user to enter daily expenses for different categories such as lodging, transportation, meals, etc.
Store daily expenses in separate numeric variables for each category.
Use the assignment operator (+=) to accumulate daily expenses into total variables for each category.
'''

for day in range(travel_days):
    meal_expenses = int(input(f'Enter meal expenses in $ for day {i}: '))
    transport_expenses = int(input(f'Enter transport expenses in $ for day {i}: '))
    accommodation_expenses = int(input(f'Enter accommodation expenses in $ for day {i}: '))
    i += 1
    total_meal_expenses += meal_expenses
    total_transport_expenses += transport_expenses
    total_accommodation_expenses += accommodation_expenses

    '''
    Exception Handling
    Use a while loop to allow the user to correct any expense entry errors.
    Ask the user if they want to make changes to the charges and allow editing of previous charges.
    Automatically update expense totals based on user changes.
    '''

    question = input('do you want to correct something? (yes or no)\n').lower()
    while question == 'yes':
        print('Choose from the possible options:\n \
                        1. "delete the last day of expense";\n \
                        2. "delete all the expenses";\n \
                        3. "cancel"')
        user_choice = int(input('Enter a number:\n'))

        if user_choice not in range(1, 3):
            break
        elif user_choice == 1:
            total_meal_expenses -= meal_expenses
            total_transport_expenses -= transport_expenses
            total_accommodation_expenses -= accommodation_expenses
            i -= 1
            print('Enter the correct expense for each category')
            meal_expenses = int(input(f'Enter meal expenses in $ for day {i}: '))
            transport_expenses = int(input(f'Enter transport expenses in $ for day {i}: '))
            accommodation_expenses = int(input(f'Enter accommodation expenses in $ for day {i}: '))
            i += 1
            total_meal_expenses += meal_expenses
            total_transport_expenses += transport_expenses
            total_accommodation_expenses += accommodation_expenses

            question = input('do you want to correct something? (yes or no)\n')

        elif user_choice == 2:
            total_meal_expenses -= 0
            total_transport_expenses -= 0
            total_accommodation_expenses -= 0
            i = 1
            print('Enter the correct expense for each category')
            meal_expenses = int(input(f'Enter meal expenses in $ for day {i}: '))
            transport_expenses = int(input(f'Enter transport expenses in $ for day {i}: '))
            accommodation_expenses = int(input(f'Enter accommodation expenses in $ for day {i}: '))
            i += 1
            total_meal_expenses += meal_expenses
            total_transport_expenses += transport_expenses
            total_accommodation_expenses += accommodation_expenses

            question = input('do you want to correct something? (yes or no)\n')

expenses = [total_meal_expenses, total_transport_expenses, total_accommodation_expenses]

'''
Calculation of total expenses
Use a for loop to iterate through the total expense variables for each category and calculate the total expense.
Store total expenses in a numeric variable.
'''

for expense in expenses:
    total_expenses += expense

'''
Results display
Print to screen a summary of total expenses for each category and the grand total of expenses.
Also show if the available budget has been respected or expenses have been exceeded.
'''

print('Here the summary of travel expenses:\n')
print('|    meal    |    transport    |    accomodation    |    total expenses    |')
print('----------------------------------------------------------------------------')
print(f'|      -{total_meal_expenses}    |         -{total_transport_expenses}      |      -{total_accommodation_expenses}            |      -{total_expenses}              |\n' )

final_budget = total_budget - total_expenses
if final_budget >= 0:
    print(f"Your initial budget covered all expenses. Here's your final budget: {final_budget}")
else:
    print(f"Your initial budget didn't cover all expenses. Here's your final budget: {final_budget}")
