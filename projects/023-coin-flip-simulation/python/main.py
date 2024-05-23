from random import choice
from math import floor

coin_faces=['H','T']
general_flip_counter=0
for i in range(10):
    same_occurence_counter=0
    flip_counter=0
    previous_result=choice(coin_faces)
    result_list=previous_result
    while same_occurence_counter<3:
        result=choice(coin_faces)
        flip_counter+=1
        result_list='{}-{}'.format(result_list,result)
        if result==previous_result:
            same_occurence_counter+=1
        else:
            same_occurence_counter=0
            previous_result=result
    print('{} ({} flips)'.format(result_list,flip_counter))
    general_flip_counter+=flip_counter
flip_average_floor=floor(general_flip_counter/10)
flip_average_ceil=flip_average_floor+1
print('On average, {} or {} flips were needed.'.format(flip_average_floor,flip_average_ceil))

