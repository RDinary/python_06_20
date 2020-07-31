def is_polyndrom(s):
    if type(s) != str:
        raise TypeError("this is not string")
    lower_s = s.lower()
    l = []
    for c in lower_s:
        if c.isalnum():
            l.append(c)
    return l == l[::-1]


print(is_polyndrom("Race Car"))
print(is_polyndrom("repaper"))
print(is_polyndrom("My gym"))
print(is_polyndrom("Red rum, sir, is murder"))
help(str)
