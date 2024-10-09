import random

max_int=random.randint(1,100)
max_int_count=1
print(f"{max_int} <== Update")

for x in range(99):
    number=random.randint(1,100)
    if number>max_int:
        max_int=number
        max_int_count+=1
        number=str(max_int)+" <== Update"

    print(number)

print(f"The maximum value found was {max_int}")
print(f"The maximum value was updated {max_int_count} times")