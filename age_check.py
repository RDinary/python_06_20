age = int(input("enter your age: "))
height = int(input("enter your height: "))
if (8 <= age < 18 and height > 115) or (age >= 18 and height > 100):
    print("go in")
else:
    print("cannot go in")

i = 2
while i % 2 == 0 and i <= 1000:
    print(i)
    i += 2
