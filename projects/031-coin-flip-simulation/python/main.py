import random
# declare a variable called sequence where store how many times flip a coin to have the same result three times in succession, and a variable where store the number of coin flip
sequence = ''
average = 0

# using a for loop run 10 times a while loop that simulate the coin flip using random int and then print results and average of coin flips needed to have three head or cross in succession 
for i in range(0,10):
    while sequence.count('TTT') == False and sequence.count('HHH') == False:
        value = random.randint(0,1)
        if value == 0:
            sequence += 'H'
        else:
            sequence += 'T'
    average += len(sequence)
    print(f'{sequence} ({len(sequence)} flips)')
    sequence = ''

print(f'On average {average / 10} were needed.')