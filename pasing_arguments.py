def add1(num):
    """
    adding 1 to num
    :param num: number
    :return: num + 1
    """
    num = num + 1
    return num


def addToList(l, v):
    l.append(v)
    return l


a = 6
add1(a)  # 7
print(a)

l1 = [2, 3, 4]
addToList(l1, 5)
print(l1)


def Print_info(name, lastname, type, money="0"):
    """
    :param name: customer's name
    :param lastname: customer's lastname
    :param type: casual/business
    :param money: amount
    :return: None
    """
    print("Hello, ", name, " ", lastname, " your account type is:", type, ". Money: ", money, sep="")
    print("Hello, " + name + " " + lastname + " your account type is:" + type + ". Money: " + str(money))
    # f-string
    print(f"Hello, {name} {lastname} your account type is: {type} Money: {money}")


Print_info("dani", "din", "casual")
Print_info("Arkadi", "Gaidamak", "business", 500000000000)


def Print(*args):
    print(type(args))
    for i in args:
        print(i)


Print(3, 4, 5, 45, 6)
