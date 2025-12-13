# function_arguments

as we know function is used to break down the code into the small parts. and make it more easier.

1.Default Arguments:{Arguments are generally specified.}
def name(first_name= "vivek", middle_name="ranjit", sir_name="kamble"):
print("The name is :",first_name,middle_name,sir_name)
name("james","lee")

2.keywords Arguments:{You can just simply change the order.}
def average(a=4,b=6):
print("The average is:", (a +b)//2)
average(b=22,a=6)

3.Required Arguments: {Must provide the value of the argument.}
def average(a,b,c=6):
print("The average is:", (a +b + c)//3)
average(1,22) {# where a = 1 & b = 22}
