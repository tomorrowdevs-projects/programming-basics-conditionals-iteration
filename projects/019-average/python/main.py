user_list = list(input('Enter your values separated by a comma:\n').split(','))
int_list = [int(i) for i in user_list]

sum = 0
counter = 0
if int_list[0] == 0:
    print("Error! First value mustn't be zero")
else:
    for value in int_list:
        if value == 0:
            break
        else:
            sum += value
            counter += 1

average = sum / counter
print(average)