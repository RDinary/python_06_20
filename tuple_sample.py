l = ["INT", "python", "course"]
t = tuple(l)
s = "INT python course"

print(l)
print(t)

print(type(l))
print(type(t))

l[1] = "JAVA"
print(l[1])

print(l)
print(t)

l.append("june")
l.append("20")

print(l)

print(s)

lst0 = [2, 1, 0]
lst1 = [0, 1, 2]
lst2 = lst0 + lst1 + lst0
print(lst2)
lst2.append(3)
print(lst2)
lst2.insert(2, 4)
print(lst2)
lst2.remove(3)
print(lst2)
lst2.remove(1)
print(lst2)

while 1 in lst2:
    lst2.remove(1)

print(lst2.count(2))

lst2_ref = lst2
print(lst2)
print(lst2_ref)
lst2[3] = 7
print(lst2)
print(lst2_ref)

print(lst2.index(7))
print(lst2.index(2))
# print(lst2.index(6))
lst2.pop()
print(lst2)
lst2.pop(0)
print(lst2)
var = lst2.pop(1)
print(lst2)
print(var)

lst2.reverse()
print(lst2)

lst_comp = lst2[::-1]
print(lst_comp)

lst_comp[0] = 6
print(lst_comp)
print(lst2)

lst2.sort(reverse=True)
print(lst2)

if 4 in lst2:
    print("4 in lst")
else:
    print("4 is not in lst")

if 6 in lst2:
    print("6 in lst")
else:
    print("6 is not in lst")

if 4 not in lst2:
    print("4 is not in lst")
else:
    print("4 in lst")

if 6 not in lst2:
    print("6 is not in lst")
else:
    print("6 in lst")
