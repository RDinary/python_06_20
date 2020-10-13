# 1 varibale and examples
'''
int  - whole num
float - decimal num
list - container of variables
str - container of chars
tuple - immutable container of variables
dictionary - key/value container
custom/class/object -  user defined type For instance Car
'''

# 2 what loop for/while?

# average list of numbers ->  for i in arr, count
# input till valid -> while
# 8 eggs weight -> for because the number is pre known

# 3 compiler/interpeter -> interpeter

# 4 bin(1.2.3.20) = 1.10.11.10100

# 5 activated program runs in RAM

# 6 12%10 = 2, 6%5 = 1, 1024 %2 =0

# 7
print(type("hello world"))

# 9
temp = True
# type = True
num1 = True
# 1num = False
_num = True
# _num = True
# class = False
# input = True
test = True
a = True

# 9
lst = ["dog", "cat", "5", "PYTHON", "INT"]
print("Hello " + lst[3] + " , Do you love " + lst[1] + " or " + lst[4])


# 10
def func(a, b):
    for i in range(len(a)):
        b.append(a[i])

#this is another change
    

# 11
print(func([1, 2, 3, 4], [4, 3, 2, 1]))

# 12
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[::-1])
print([lst[5:]])

# 13
a = 5
b = 10
c = 7
if a % 5 == 0 and b % 5 == 0:
    print("1")
    if c == 2 or a < 10:
        print("2")
    else:
        print(3)
else:
    print(4)
print("5")


# 15 - errors question

# 16
def func(a):
    return a * 2
    print(a * 3)


num = 5
print(num)
print(func(num))

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for i in range(10):
    if i % 2 == 0:
        print(num[i - 1])
    if i % 3 == 0:
        print(letter[i])


# 18
# what is self => self is this instance to the class

# 20


# 21 what is init => creating instance/object of this class

# 22 what is encapsulation -> hide class properties

# part 2:
def max_two(arr):
    if len(arr) < 2:
        print("too small array")
    max1 = max(arr)
    arr.remove(max1)
    max2 = max(arr)
    return max1, max2


def func2():
    try:
        result = int(input("please enter numer"))
    except ValueError:
        pass


def func3(names_arr):
    name = input("enter name: ")
    if name in names_arr:
        print(names_arr.index(name))
    else:
        print("not in list")


from random import randint


def func4():
    arr = []
    for i in range(100):
        arr.append(randint(0, 10))
    return arr


print(func4())


class student:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__marks = []

    def addMark(self, mark):
        self.__marks.append(mark)

    def avg_mark(self):
        return sum(self.__marks) / len(self.__marks)


def legalemail(email):
    if email.count('@') != 1:
        return False
    for c in email:
        if c.isalnum() or c == '.' or c == '@':
            continue
        return False
    return True
