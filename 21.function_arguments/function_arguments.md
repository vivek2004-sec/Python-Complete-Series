# function_arguments

as we know function is used to break down the code into the small parts. and make it more easier.

1.Default Arguments:
In this we give pre-defined values to the function parameters.and python uses it automatically.
-> non-default arguments cannot come after default arguments.
-> For Eg: def average(b, a = 4) in this non-default argument came first.

2.keywords Arguments:
You can just simply change the order. but we have to explicitly specify the arguments very carefully.
def average(a=4,b=6):
print("The average is:", (a +b)//2)
average(b=22,a=6)

3.Required Arguments: {Must provide the value of the argument.}
def average(a,b,c=6):
print("The average is:", (a +b + c)//3)
average(1,22) {# where a = 1 & b = 22}
