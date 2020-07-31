class flour:
    def __init__(self, origin):
        self.__origin = origin

    def get_origin(self):
        return self.__origin


class eggs:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size


class chocho:

    def __init__(self, is_dairy):
        self.__is_dairy = is_dairy

    def is_dairy(self):
        return self.__is_dairy

    def __str__(self):
        if self.__is_dairy:
            return "tasty dairy chocholate"
        else:
            return "next time my friend"


class choco_cookie:

    def __init__(self, Flour, Eggs, Chocho):
        self.flour = Flour
        self.eggs = Eggs
        self.__choco = Chocho

    def get_choco(self):
        return self.__choco


f = flour("wheat")
e = eggs("L")
c = chocho(True)

f1 = flour("Spelt")
c1 = chocho(False)

c_cookie = choco_cookie(f, e, c)  # composition
d_cookie = choco_cookie(f1, e, c1)  # composition
print(c_cookie.get_choco())
print(d_cookie.get_choco())
