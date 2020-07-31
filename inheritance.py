class cloth:
    def __init__(self, size, colour, model, fabric, madein="china"):
        self.__size = size
        self.__color = colour
        self.__model = model
        self.__fabric = fabric
        self.__madein = madein

    def get_size(self):
        return self.__size

    def set_size(self, correct_size):
        self.__size = correct_size

    def get_colour(self):
        return self.__color

    def set_colour(self, correct_colour):
        self.__color = correct_colour

    def get_fabric(self):
        return self.__fabric

    def get_model(self):
        return self.__model

    def set_model(self, correct_model):
        self.__model = correct_model

    def __str__(self):
        return f"size: {self.__size}, fabric: {self.__fabric}," \
               f" colour: {self.__color}, model: {self.__model}, made in: {self.__madein}"


class shirt(cloth):
    pass


class pants(cloth):
    pass


class socks(cloth):
    pass


class coat(cloth):
    def __init__(self, size, colour, model, fabric, rain_resistance, madein="Taiwan"):
        super().__init__(size, colour, model, fabric, madein)
        self.__rain_resistance = rain_resistance

    def __str__(self):
        return f"{super().__str__()}, rain_resistance: {self.__rain_resistance}"


s = shirt("L", "Black", "Hawaii", "silk")
print(s)
p = pants("L", "Black", "Hawaii", "silk")
print(p)
c = coat("L", "Black", "Hawaii", "silk", False)
print(c)

print(c.get_colour())
