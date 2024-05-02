num_days = int(input("What's the number of travel days? "))
budget = float(input("What's your total budget? "))

tot_lodging = tot_transport = tot_meals = 0.0
lodging_ls = '_'
transport_ls = '_'
meals_ls = '_'

for day in range(1, num_days + 1):
    print(f'Day {day}: ')
    lodging = input("Lodging expense for this day: ")
    transport = input("Transportation expense for this day: ")
    meals = input("Meals expenses for this day: ")

    lodging_ls += f'{lodging}_'
    transport_ls += f'{transport}_'
    meals_ls += f'{meals}_'

    tot_lodging += float(lodging)
    tot_transport += float(transport)
    tot_meals += float(meals)

answer = 'yes'
while answer.lower() == 'yes':
    answer = input('Do you want to make any change? (yes/no) ')
    if answer.lower() != 'yes':
        print('Exiting . . .\n\n')
        continue
    change_category = input('What category do you want to change? (lodging/transportation/meals) ')
        
    if change_category.lower() == 'lodging':
        day_to_change = int(input('Enter the day: '))
        new_charge = float(input('Enter enter the new charge: '))

        separator_count = 0
        for index_lodging in range(0, len(lodging_ls)):
            if lodging_ls[index_lodging] == '_':
                separator_count += 1
                if separator_count == day_to_change: 
                    sliced_lodging_ls = lodging_ls[index_lodging + 1:]
                
        separator_count = 0
        for second_index_lodging in range(0, len(sliced_lodging_ls)):
            if sliced_lodging_ls[second_index_lodging] == '_':
                separator_count += 1
            if separator_count == 1:
                old_charge_lodging = sliced_lodging_ls[:second_index_lodging]
        
        tot_lodging -= float(old_charge_lodging)
        tot_lodging += new_charge

    elif change_category.lower() == 'transportation': 
        day_to_change = int(input('Enter the day: '))
        new_charge = float(input('Enter the new charge: '))

        separator_count = 0
        for index_transport in range(0, len(transport_ls)):
            if transport_ls[index_transport] == '_':
                separator_count += 1
                if separator_count == day_to_change: 
                    sliced_transport_ls = transport_ls[index_transport + 1:]
        
        separator_count = 0
        for second_index_transport in range(0, len(sliced_transport_ls)):
            if sliced_transport_ls[second_index_transport] == '_':
                separator_count += 1
                if separator_count == 1:
                    old_charge_transport = sliced_transport_ls[:second_index_transport]
        
        tot_transport -= float(old_charge_transport)
        tot_transport += new_charge

    elif change_category.lower() == 'meals':
        day_to_change = int(input('Enter the day: '))
        new_charge = float(input('Enter the new charge: '))

        separator_count = 0
        for index_meals in range(0, len(meals_ls)):
            if meals_ls[index_meals] == '_': 
                separator_count += 1
                if separator_count == day_to_change:
                    sliced_meals_ls = meals_ls[index_meals + 1:]
        
        separator_count = 0
        for second_index_meals in range(0, len(sliced_meals_ls)): 
            if sliced_meals_ls[second_index_meals] == '_':
                separator_count += 1
                if separator_count == 1:
                    old_charge_meals = sliced_meals_ls[:second_index_meals]
        
        tot_meals -= float(old_charge_meals)
        tot_meals += new_charge
    else: 
        print('Error. Make sure you have entered the correct word.')
        continue

grandtotal = 0
for total in (tot_transport, tot_lodging, tot_meals): 
    grandtotal += total

print(f'Total expense for:\n-Lodging: €{tot_lodging:.2f}\n-Transportation: €{tot_transport:.2f}\n-Meals: €{tot_meals:.2f}\n\nGrandtotal: €{grandtotal:.2f}')

if grandtotal > budget: 
    print("Warning: your expenses exceed your budget.")
else:
    print("You stayed in your budget!")

        

    





