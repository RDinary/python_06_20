def Max(arr):
    pass


def Min(arr):
    pass


def Add(arr, value):
    pass


def Remove(arr, value):
    pass


def Sort(arr, asc):
    '''
    :param arr: array to be sorted
    :param asc: bool. if true sort by ascending order, else by descending order
    '''
    pass


def Average(arr):
    pass


def Index(arr, value):
    pass


def Count(arr, value):
    pass


def missing_numbers(arr):
    pass


def refill(arr):
    '''
    insert 500 random numbers to arr
    '''
    pass


def Menu():
    arr = [2, 3, 4, 4, 4, 4, 4, 4, 4]
    print("for min press 1, for max press 2 ...")
    choice = int(input("enter your choice"))
    if choice == 1:
        Min(arr)
    elif choice == 2:
        Max(arr)
