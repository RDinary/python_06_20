max_msg = "The maximum number from:"


def max_of_two(a, b):
    if a > b:
        print(max_msg, a, b, "is:", a)
    else:
        print(max_msg, a, b, "is:", b)


def max_of_three(a, b, c):
    max_num = 0
    if a > b:
        if a < c:
            max_num = c
        else:
            max_num = a
    else:
        if b > c:
            max_num = b
        else:
            max_num = c
    print(max_msg, a, b, c, "is:", max_num)


max_of_two(3, 4)
max_of_two(5, 2)

max_of_three(1, 3, 5)
max_of_three(1, 5, 3)
max_of_three(3, 5, 1)
max_of_three(5, 3, 1)  # wrong result
max_of_three(5, 1, 3)  # wrong result
max_of_three(5, 5, 5)
