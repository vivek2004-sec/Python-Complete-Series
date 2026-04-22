# Adding Elements into List
ls = []

ls.append(1)
print(ls)

ls.insert(1, 2)
print(ls)

ls.extend([3, 4, 5])
print(ls)

# Updating Elements into List

a = [1, 2, 3, 4, 5]
a[1] = 6
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# Removing Elements from List

a = [10, 20, 30, 40, 50]
a.remove(40)
print(a)
a.pop(1)
print(a)
del a[0]
print(a)
a.clear()
print(a)


a = [1, 2, 3, 4, 5, 6,6,6]
print(len(a))
print(a.index(5))
print(a.count(6))
a.reverse()
print(a)
b = a.copy()
print(b)


# Iterating Over Lists


lst = ["mango", 'apple', 'orange', 'kiwi']
for fruits in lst:
    print(fruits)
    
    
# Nested Lists:

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])


# List Comprehension
# List comprehension provides a concise way to create lists in a single line of code.
# It is commonly used to apply an operation or condition to elements of an iterable, such as a list, tuple, or range.


squares = [ x**2 for x in range(1, 6)]
print(squares)
