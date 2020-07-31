class Item:
    """
    item class docstring
    """

    def __init__(self, name, price, code):
        self.__name = name
        self.__price = price
        self.__code = code

    def PrintInfo(self):
        print(f"Item name: {self.__name}, price: {self.__price}, Code: {self.__code}")

    def __str__(self):
        return "__str__"
        # return f"Item name: {self.__name}, price: {self.__price}, Code: {self.__code}"

    def rename(self, newname):
        self.__name = newname


item1 = Item("milk", 5, 2901290)
item2 = Item("mask", 15, 00000000)

item1.PrintInfo()
item2.PrintInfo()

item2.rename("KN95")
item2.PrintInfo()

item1.rename("low fat milk")
item1.PrintInfo()

print(item1)

print(1 + 2)
print("1" + "2")
print(type(item2))
