year_of_birth = int(input("enter your year of birth"))

if year_of_birth == 2014:
    print("1st grade")
elif year_of_birth == 2013:
    print("2nd grade")
elif year_of_birth == 2012:
    print("3rd grade")
elif year_of_birth == 2011:
    print("4th grade")

l = [3, 6, 1, 7, 90, 2, 5, 10]
i = 0  # index
list_len = len(l)
while i < list_len:
    j = 0  # index
    while j < list_len - 1:
        if l[j + 1] < l[j]:
            tmp = l[j + 1]
            l[j + 1] = l[j]
            l[j] = tmp
        j += 1
    i += 1
print(l)
