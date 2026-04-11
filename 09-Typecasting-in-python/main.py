# a = "1"
# b = "2"
a = 1
b = 2

sum= a + b

print("the sum is: ", sum)


'''
Typecasting in Python:

The conversion of one data type into the other data type is known as type casting in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(),
list(), set(), dict(), etc.
'''
a= "10"
b= "5"

print(int(a) + int(b))

a= 12
b= 5

print(str(a) + str(b))

# Explicit Typecasting:

string= "15"
number= 7

string_number = int(string)

sum= number + string_number
print("the sum is: ", sum)

# Implicit Typecasting:

c= 1.9
d= 8

print(int(c) +d)

print("the type of c is", type(c))
print("the type of d is", type(d))

# Explicit 
A = "7"
B = 9

string= int(A)

sum = string + B

print("sum is:", sum)

# implicit

t=5.6
u= 7

print(int(t) + u)


