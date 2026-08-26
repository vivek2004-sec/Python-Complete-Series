# Generators: Python generators are simple way of creating iterators.

L  = [x for x in range(10000)]

# for i in L:
#     print(i**2)
    
import sys

print(sys.getsizeof(L)) # gives size in bytes.

x = range(10000000)
print(sys.getsizeof(x))