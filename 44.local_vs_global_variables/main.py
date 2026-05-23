


# name = "Vivek"        # global variable

# def my_function():
#     name = "Kamble"   # local variable (different!)
#     print(name)       # prints local

# my_function()
# print(name)           # prints 


# x = 5

# def vue():
#     x = 7
#     print(x)

# vue()
# print(x)


# x = 7

# def rishi():
#     y = 8
#     print(y)


# rishi()
# print(x)
# print(y)  Throws an error as y is local variable and cannot be exist outside the function.


# Gobal Keyword:

name = "kamble"

def my_name():
    global name
    name = "vivek"
    print(name)

my_name()
print(name)