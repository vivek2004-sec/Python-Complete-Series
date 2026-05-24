add = lambda a, b: a + b

print(add(5, 3))   # 8


aor = lambda l, b: l*b

print("Area of reactangle is:",aor(3,4))


area_of_square = lambda s: s**2

print("Area of square is: ", area_of_square(5))


is_even = lambda x: x % 2 == 0
print(is_even(4))       # True
print(is_even(5))       # False


maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # 20


greet = lambda: "Hello Vivek!"
print(greet())          # Hello Vivek!

# map() applies function to each item in list

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)          # [1, 4, 9, 16, 25]


arr = [1,2,3,4]

vue = list(map(lambda x: x*4, arr))
print(vue)


# filter() filters items based on condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)            # [2, 4, 6, 8]


# sort list of tuples by second element

students = [("Vivek", 21), ("John", 19), ("Sara", 22)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# [('John', 19), ('Vivek', 21), ('Sara', 22)]


from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)
print(total)            # 15  (1+2+3+4+5)