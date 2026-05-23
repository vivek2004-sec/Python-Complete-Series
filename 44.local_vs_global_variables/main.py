


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

name = "Vivek"        # global variable

def my_function():
    global name       # ← tells Python use GLOBAL variable
    name = "Kamble"   # modifies the GLOBAL variable
    print(name)

my_function()
print(name)           # global variable is now changed!



count = 0

def increment():
    global count        # ✅ use global count
    count = count + 1
    print(count)

increment()
increment()
increment()
print(count)