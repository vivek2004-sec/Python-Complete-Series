x = 4
print(x)

def hello():
    x = 5
    print(f"The local variable is {x} ")
    print("Hello!")
    
print(f"The local variable is {x}")
hello()
print(f"The global variable is {x}")