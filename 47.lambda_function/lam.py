# map 


l = [1, 2, 3, 44, 5, 66]

square = list(map(lambda s: s**2, l))
print(square)


# filter

is_small = list(filter(lambda a: a > 3, l))
print(is_small)