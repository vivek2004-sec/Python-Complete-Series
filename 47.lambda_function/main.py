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