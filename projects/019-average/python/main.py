sum = 0
counter = 0
user_value = int(input('Enter a number (must be different from zero):\n'))
if user_value == 0:
    print("Error! First value mustn't be zero")

while user_value != 0:
    sum += user_value
    counter += 1
    user_value = int(input('Enter a number (must be different from zero):\n'))


average = sum / counter
print(average)
