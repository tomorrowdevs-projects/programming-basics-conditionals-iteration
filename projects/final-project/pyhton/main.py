
travel_days = int(input('Insert number of travel day: '))
u_budget = int(input('Insert the total budget for the trip: '))
total_lodging = 0
total_transportation = 0
total_meals = 0

for n_day in range(travel_days):
    is_correct = False

    while is_correct == False:
        u_lodging = int(input(f'Insert the lodging expanses of day {n_day +1}: '))
        u_transportation = int(input(f'Insert the trasportation expanses of day {n_day +1}: '))
        u_meals = int(input(f'Insert the meals expanses of day {n_day +1}: '))

        is_question = False

        while is_question == False:
            user_question = input(f'Do you want to change any expanse entry of the day {n_day +1}? (yes/no): ').lower()
        
            if user_question == 'no':
                is_correct = True
                is_question = True
            
            elif user_question == 'yes':
                print(f'Modify the expanse entry of the day {n_day +1}')
                is_question = True
            
            else:
                print('Please, enter "yes" or "no"')

    total_lodging += u_lodging
    total_transportation += u_transportation
    total_meals += u_meals
        
total_trip = total_lodging + total_transportation + total_meals

print(f'Total lodging expanses: {total_lodging}')
print(f'Total transportation expanses: {total_transportation}')
print(f'Total meals expanses: {total_meals}')
print(f'Total trip expanses: {total_trip}')

respected_budget = u_budget - total_trip

if respected_budget >= 0:
    print(f'The budget was respected, {respected_budget}€ was left')

else:
    print(f'The budget was not respected, {(respected_budget*(-1))}€ more were used')

