a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # False — different objects, even though values are same
print(a == b)  # True - defferent objects, but same values.


a = 3
b = 3

print(a == b) # True
print(a is b) # False

m = [3]
n = [3]

print(m == n) # True if values are same .
print(m is n) # False even if values are same but points the different object.


# Always use :

x = None

if x is None:
    print("x is none.")