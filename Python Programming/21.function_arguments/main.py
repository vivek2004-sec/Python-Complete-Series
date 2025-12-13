# def average(a,b):
#     print("The average is:", (a +b)//2)
# average(4,6)

# def name(first_name= "vivek", middle_name="ranjit", sir_name="kamble"):
#     print("The name is :",first_name,middle_name,sir_name)
# name("james","lee")

# def average(a=4,b=6):
#     print("The average is:", (a +b)//2)
# average(b=22,a=6)


# def average(a,b,c=6):
#     print("The average is:", (a +b + c)//3)
# average(1,22)

# def average (*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
        
#     print("Average is:", sum / len(numbers))

# average(5,6, 9,11, 7)

# def name(**name):
#     print(type(name))
#     print("Hello",name["fname"], name["mname"],name["lname"])
# name(mname = "Ranjit", lname="kamble", fname="vivek")


def average (*numbers):
#     print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        
    return  sum / len(numbers)
#  
  

c = average(5,6, 9,11, 7)
print(c)