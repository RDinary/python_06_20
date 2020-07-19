print("|", end="")
for i in range(3, 8):
    print("i =", i, end="->", sep="|")
print()
for j in range(3, 8, 2):
    print("j =", j, end=" ", sep="/")
print()
for k in range(5):
    print("k =", k, end="%")
print()
for l in range(8, 3, -2):
    print("l =", l, end="\"")

list = [5, 6, 7, 8]
for i in list:
    print(i)
