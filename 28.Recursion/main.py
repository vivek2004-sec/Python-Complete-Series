def factorial (n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

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
print(fibonacci(5))


def fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(6))


# sum of n numbers

def sum(n):
    '''It takes n numbers and adds them so that we can get our desired output.'''
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
print(sum.__doc__)
print(sum(5))


# Product of n numbers

def product(n):
    '''It Multiplies numbers we gave him.'''
    if n == 0:
        return 1
    else:
        return n * product(n-1)
    
print(product.__doc__)
print(product(7))

#  USD $ TO INR CONVERSION

def money_converter(n):
    i = 94.20
    money = i * n
    return money

print(money_converter(10))
print(money_converter(2))


# Even 

def even_num(n):
    # even_num = n % 2 == 0
    # a = even_num
    # print(a)
    if n % 2 == 0:
        print(even_num(),"Given number is Even.")
        
even_num(6)


# odd 
def odd_num(n):
     if n % 2 != 0:
        print(odd_num(), "Given number is odd.")
   
   
odd_num(7)     
    