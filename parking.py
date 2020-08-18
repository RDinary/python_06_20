import time

username = "admin"
password = "admin"


class car:
    def __init__(self, plate, phone_number, arrival_time):
        self.__plate = plate
        self.__phone = phone_number
        self.__arrival_time = arrival_time

    def get_plate(self):
        return self.__plate

    def set_plate(self, plate):
        self.__plate = plate

    def get_arrival_time(self):
        return self.__arrival_time

    def __str__(self):
        return f"plate: {self.__plate}, phone: {self.__phone}," \
               f" day: {self.__arrival_time.tm_mday} at {self.__arrival_time.tm_hour}"


class ParkingLot:

    def __init__(self):
        self.__price = 15
        self.__capacity = 10
        self.__cars = []  # empty list

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"price: {self.__price}, free capacity: {self.__capacity - len(self.__cars)}"

    def add_car(self, c):
        c_plate = c.get_plate()  # plate number of coming car
        for vehichle in self.__cars:
            if vehichle.get_plate() == c_plate:  # if there is car with same plate in
                print("this car is already inside")
                return 0  # go out, there is no reason to continue in this function
        self.__cars.append(c)

    def print_cars_in_parking_lot(self):
        print("printing cars in parking lot")
        for parked_car in self.__cars:
            print(parked_car)

    def report_24(self):
        now = time.gmtime()  # time now
        for parked_car in self.__cars:
            if parked_car.get_arrival_time().tm_yday < now.tm_yday:
                print(parked_car)


def user_create_car():
    plate = input("enter plate number")
    phone = input("enter phone number")
    arrive = time.gmtime(int(input("enter arrival time")))
    return car(plate, phone, arrive)


t1 = time.gmtime(1289348934)

c1 = car(plate="127001", phone_number="05050505", arrival_time=t1)
c2 = car("2383490", "9054", time.gmtime(231345233))

parklot = ParkingLot()

parklot.add_car(c1)
parklot.add_car(c2)

i = 0
while i < 7:
    i += 1
    if i == 10:
        break
    if i % 2 == 0:
        continue
    print(i)
print("breaked")

age = 21
if age > 18:
    print("you are allowed in club")
elif age > 12:
    print("you are allowed in superland")
else:
    print("everybody getting older")

try:
    515602300320561603 / 0
except ZeroDivisionError:
    print("zero division")
except:
    print("got oyu")
