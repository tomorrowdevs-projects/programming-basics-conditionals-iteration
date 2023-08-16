import random

red_list = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_list = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green_list = [0, '00']
list_number = list(range(37)) + ["00"]

random_number = random.choice(list_number)
print(random_number)
if random_number in red_list:
    if random_number % 2 == 0:
        if random_number in range(19):
            print(
                f"The spin resulted in {random_number}...\n"\
                f"Pay {random_number}\n"\
                "Pay red\n"\
                "Pay even\n"\
                "Pay 1 to 18"
                )
        else:
            print(
                f"The spin resulted in {random_number}...\n"\
                f"Pay {random_number}\n"\
                "Pay red\n"\
                "Pay even\n"\
                "Pay 19 to 36"
                )
    else:
        if random_number in range(19):
            print(
                f"The spin resulted in {random_number}...\n"\
                f"Pay {random_number}\n"\
                "Pay red\n"\
                "Pay odd\n"\
                "Pay 1 to 18"
                )
        else:
            print(
                f"The spin resulted in {random_number}...\n"\
                f"Pay {random_number}\n"\
                "Pay red\n"\
                "Pay odd\n"\
                "Pay 19 to 36"
                )
elif random_number in green_list:
    if random_number == 0:
        print("Pay 0")
    else:
        print("Pay 00")
else:
    if random_number % 2 == 0:
        if random_number in range(19):
            print(
                f"The spin resulted in {random_number}...\n"\
                f"Pay {random_number}\n"\
                "Pay black\n"\
                "Pay even\n"\
                "Pay 1 to 18"
                )
        else:
            print(
                f"The spin resulted in {random_number}...\n"\
                f"Pay {random_number}\n"\
                "Pay black\n"\
                "Pay even\n"\
                "Pay 19 to 36"
                )
    else:
        if random_number in range(19):
            print(
                f"The spin resulted in {random_number}...\n"\
                f"Pay {random_number}\n"\
                "Pay black\n"\
                "Pay odd\n"\
                "Pay 1 to 18"
                )
        else:
            print(
                f"The spin resulted in {random_number}...\n"\
                f"Pay {random_number}\n"\
                "Pay black\n"\
                "Pay odd\n"\
                "Pay 19 to 36"
                )
