# Python Functions:

# Python Functions are a block of statements that does a specific task.
# The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code,
# again and again for different inputs, 
# we can do the function calls to reuse code contained in it over and over again.

# Uses:
# Code Reusability.
# Modularity.
# Readability.
# Maintainability.


def gmean(a, b):
    gmean = (a*b)/(a+b)
    print(gmean)
    
def isgreater(a,b):
    if (a >b):
        print("a is greater than b.")
    else:
        print("b is greater than a.")

    
    
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

isgreater(a,b)
gmean(a,b)

c = 12
d = 5
isgreater(c,d)
gmean(c,d)

def evenodd(a):
    if (a % 2 == 0):
        print("even")
    else:
        print("odd")
    
a = 4
evenodd(a)

m = 5
evenodd(m)

def area_of_triangle(b, h):
    area_of_triangle = b*h/2
    print(area_of_triangle)

b = int(input("Enter the base: "))
h = int(input("Enter the height: "))

area_of_triangle(b, h)

def area_of_circle(r):
    area_of_circle = 3.14 * r*r
    print(area_of_circle)

r = int(input("Enter the radius: "))

area_of_circle(r)


def area_of_rectangle(l, b):
    area_of_rectangle = l * b
    print(area_of_rectangle)

l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))

area_of_rectangle(l, b)