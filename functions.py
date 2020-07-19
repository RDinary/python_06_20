def my_func():
    print("my func")


def print_hello(name):  # definition
    print("hello", name)


print_hello("Vitali")  # call
other_name = "Rafi"
print_hello(other_name)
your_name = "moti"
print_hello(your_name)
other_name = "dani"

my_func()


def add_one(num):
    print(num + 1)


add_one(7)
add_one(8.32)


def my_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


testlist = [3, 4, 5, 6, 7]

print(my_len(testlist))
