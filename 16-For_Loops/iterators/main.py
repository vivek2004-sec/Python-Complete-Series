# Iteration : It means taking each element of something one by one. any time you use the loop.

# num = [1, 2, 3]
# for i in num: 
#     print(i * 2 )
    
# Iterator:  an iterator is an object that allows a programmer to traverse through a sequence of data without having to store the entire 
# data in memory.
import sys
# x = [ l for l in range(1, 10000)]

# for i in x:
#     print(x * 2)



# print(sys.getsizeof(x)/8)

x = range(1, 10000)

# for i in x:
#     print(i * 2)
    
print(sys.getsizeof(x))

# Iterable: object which one can iterate over.