user_bit = input("Enter 8 bit (newline character to quit):\n")

while True:
    if user_bit == "":
        break
    elif len(user_bit) != 8 or not all(i in ['0', '1'] for i in user_bit):
        break

    count_bit_1 = user_bit.count("1")

    if count_bit_1 % 2 != 0:
        print(1)
    else:
        print(0)

    user_bit = input("Enter 8 bit (newline character to quit):\n")