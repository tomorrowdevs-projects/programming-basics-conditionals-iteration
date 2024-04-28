from random import choice

coin_faces=['H','T']
simulation_counter=0
general_flip_counter=0
while simulation_counter<10:
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
    simulation_counter+=1
flip_average=general_flip_counter/10
print('On average, {} flips were needed.'.format(flip_average))

