"""
4 list functions are allowed to use:
insert, pop, remove, append
operatros: in, not in
"""


def Max(arr):
    """
    Max([2,3,4,5])
    5
    """
    # return!!!
    pass


def Min(arr):
    pass


def Add(arr, value):
    pass


def Remove(arr, value):
    """
    removes first occcurence of value in arr
    :param value: value to be removed
    :return:
    """
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
    arr_special = [2, 3, 4, 4, 4, 4, 4, 4, 4]
    print("for min press 1, for max press 2 ...")
    choice = int(input("enter your choice"))
    if choice == 1:
        Min(arr_special)
    elif choice == 2:
        Max(arr_special)


if __name__ = "__main__":
    Menu()
