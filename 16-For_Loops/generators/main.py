# Generators: Python generators are simple way of creating iterators.

L  = [x for x in range(10000)]

# for i in L:
#     print(i**2)
    
import sys

print(sys.getsizeof(L)) # gives size in bytes.

x = range(10000000)
print(sys.getsizeof(x))

# example of Generator

# generator is an actual function which has yield statement instead of return statement.

def gen_rt():
    yield "First statement"
    yield "Second statement"
    yield "Third statement"
    
    
gen = gen_rt()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))