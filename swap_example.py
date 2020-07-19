a = 7
b = 3
# swap
tmp = a
a = b
b = tmp

print("a = ", a)
print("b = ", b)

i = 0
while i < 10:
    i += 1
    print("i = ", i)

print("i = ", i)

list1 = ["flour", "eggs", "chocolate", "water", "coconut", "candies"]
list2 = [4, 8, 12, 3, 6, 8]
length = len(list1)
print("len of list", length)

for elm in list1:
    print(elm)
print("finished loop")

i = 0
while i < len(list1):
    print(list1[i], list2[i])
    i += 1
