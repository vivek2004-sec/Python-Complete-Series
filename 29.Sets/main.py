
se = {2, 4, 2, 6}
print(se)
print(type(se))




num = {1, 3, 3, 4, 4}
num.add(2)
print(num)

# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)


sv = {"Geeks", "for", 10, 52.7, True}
print(sv)


# Normal set (mutable)
s = set(["a", "b", "c"])
print("Normal Set:", s)

# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)