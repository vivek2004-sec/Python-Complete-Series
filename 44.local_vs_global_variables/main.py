


# name = "Vivek"        # global variable

# def my_function():
#     name = "Kamble"   # local variable (different!)
#     print(name)       # prints local

# my_function()
# print(name)           # prints 


x = 5

def vue():
    global x
    x = 7
    print(x)

vue()
print(x)


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


# Question: 
# Create a program that:
# → Has a global score = 0
# → Has a function add_score(points)
#    that adds points to score
# → Has a function reset_score()
#    that resets score to 0
# → Print score after every call

# Expected Output:
# Score → 10
# Score → 30
# Score → 60
# Score → 0   ← after reset


score = 0

def add_score(points):
    global score
    score += points
    print(score)
    
def reset_score():
    global score
    score = 0 
    print(score)


add_score(10)
add_score(20)
add_score(30)
reset_score()



