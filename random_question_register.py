#随机出几个数字,然后进行二十次加减

import random
def random_produce_funcation():
    random_list=[]
    number_sum=0

    for number in range(20):
        random_list.append(random.randint(0, 100000))

    for i in random_list:
        number_sum=i+number_sum

    print(random_list)
    print(number_sum)

    return random_list,number_sum