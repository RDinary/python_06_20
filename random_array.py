from random import randint


def create_random_array(min_rand, max_rand, count):
    l = []
    for _ in range(count):
        l.append(randint(min_rand, max_rand))
    return l


elem_num = int(input("enter number of elements: "))
min_num = int(input("enter minimum: "))
max_num = int(input("enter maximum: "))
l = create_random_array(min_num, max_num, elem_num)

print(l)
