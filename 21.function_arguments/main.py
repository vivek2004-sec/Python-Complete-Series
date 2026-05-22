# Default Arguments: 
# 1.
def average(a =4,b=6):
    print("The average is:", (a +b)//2)
average()

# 2.
def aor(l,b=4):
    aor = l*b
    print(aor)
aor(3)


#  Keyword Arguments:

def name_of_std(fname, mname, lname ):
    print(fname, mname, lname)

name_of_std(lname = 'kamble', fname = 'rishi', mname = 'ranjit')

def sum_of_num(a, b, c, d):
    print("The sum is: ",  a+b+c+d)

sum_of_num(b=4, c=6, d=9, a=1)

def average(a=4,b=6):
    print("The average is:", (a +b)//2)
average(b=22,a=6)


# Postional Arguments:

def name(fname, mname, lname):
    print(fname, mname, lname)

name("vivek", "Ranjit", "kamble.")

# variable_length Argument:

def average (*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        
    print("Average is:", sum / len(numbers))

average(5,6, 9,11, 7)

def mean(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print("Mean is: ", sum//len(numbers))
    
mean(1,2,3,4,5,6,7)


# Keyword_variable length argument:
def name(**name):
    print(type(name))
    print("Hello",name["fname"], name["mname"],name["lname"])
name(mname = "Ranjit", lname="kamble", fname="vivek")


def average (*numbers):
#     print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        
    return  sum / len(numbers)
#  
  

c = average(5,6, 9,11, 7)
print(c)


def f1():
    s = "I love YOU."
    def f2():
        print(s)
        
    f2()
f1()
   

def area(l, b):
    def aor():
        aor = l*b
        print(aor)
    aor()

area(4,5)

# return: sends value back to the calling function.

def sum(a, b):
    return a + b

x = sum(2,3)
print(x)

# Pass by Reference and Pass by Value
'''
Variables are references to objects. When we pass them to a function, behavior depends on whether the object is mutable (like lists, dictionaries) or immutable (like integers, strings, tuples).

Mutable objects: Changes inside the function affect the original object.
Immutable objects: The original value remains unchanged.'''

def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   

def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)


def my(lst):
    lst.append(7)

a = [1,2,3]
my(a)
print(a)


def my1(x):
    name = 'vivek'

x = 'rishi'
my1(x)
print(x)

'''
 # Recursive Functions
A recursive function is a function that calls itself to solve a problem. 
It is commonly used in mathematical and divide-and-conquer problems. 
Always include a base case to avoid infinite recursion.'''


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

countdown(5)
        
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(9))


