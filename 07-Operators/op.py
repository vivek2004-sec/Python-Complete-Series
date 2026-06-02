a = 10000
b = 10000
print(a == b)   # True  → same value
print(a is b)   # False → different objects (no caching above 256)


a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b)
'''
Here a == b says that a and b both contains same values.
and a is b says both are different lists located in memory.
'''
a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a is not b)

m = [1,2]
n = m
print(m is n)
print(m is not n)