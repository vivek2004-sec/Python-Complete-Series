# Adding Elements to set:

cities = {"Mumbai", "Delhi", "Pune", "Kolhapur", "Banglore", "Hyderabad"}
cities.add("Gurgaon")
print(cities)

# Removing Elements from set:

cities.remove("Delhi")
print(cities)

# Union of Sets:

x = {'a', 'b', 'c'}
y = {'d', 'e', 'f'}

u = x.union(y)
print(u)


# Intersection of Sets:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

v = a.intersection(b)
print(v)

# Difference of Sets: returns the values which are present in the first set but not in the second set.

a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)