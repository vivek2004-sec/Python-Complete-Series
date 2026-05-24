# map 


l = [1, 2, 3, 44, 5, 66]

square = list(map(lambda s: s**2, l))
print(square)


# filter

is_small = list(filter(lambda a: a > 3, l))
print(is_small)

# reduce 


from functools import reduce

sum = (reduce(lambda v,w : v + w , l))
print(sum)

import os
os.mkdir("48.is_vs_==")