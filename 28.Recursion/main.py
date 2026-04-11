# def factorial (n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# f0 = 0
# f1 = 1
# f2 = f0 + f1
# f(n) = f(n-1) + f(n-2)
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1: 
        return 1
    else :
        return  fibonacci(n-1) +fibonacci( n-2)
print(fibonacci(8))
print(fibonacci(2))
print(fibonacci(55))
print(fibonacci(13))
