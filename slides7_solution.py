def sum_divided_by_mutli(*args):
    """
    :param *args numbers to be summed and mutiplied
    :return sum of args divided by their multipication
    """
    sum = 0
    mul = 1
    if 0 in args:
        raise ZeroDivisionError("no value in arguments can be 0")
    for i in args:
        try:
            i = float(i)
        except ValueError:
            print(f"list must contain only numbers - ignoring value of {i}")
        if i == 0:
            raise ZeroDivisionError("no value in arguments can be 0")
        sum += i
        mul *= i
    return sum / mul


try:
    res = sum_divided_by_mutli(2.43, -239, -239, 8)
except ZeroDivisionError:
    print("mistake")  # do something.
print(res)

d = {"flour": 2, "eggs": 5, "chocolad": 6}

for k, v in d.items():
    print(k, v)
