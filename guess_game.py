from random import randint

low = int(input("enter low number"))
high = int(input("enter high number"))

random_num = randint(low, high)

while True:
    guess = int(input("enter your guess"))
    if guess > random_num:
        print("enter lower number")
    elif guess < random_num:
        print("enter higher number")
    else:
        print("this is it!")
        break
