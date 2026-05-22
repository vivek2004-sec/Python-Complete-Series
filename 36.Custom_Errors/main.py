# a = int(input("Enter any value between 5 and 9: "))
# if a >= 5 or a <= 9:
#     raise ValueError ("value should be between 5 and 9")


# vue = [1,23,4,55,56,45,33]
# print(len(vue))
# i = int(input("Enter the num: "))
# if i == len(vue):
#  raise IndexError ("Index is not correct.")

# n = str(input("Enter the string :"))
# if n != "quit" :
#     raise TypeError("The string is not correct.")
    
# else: 
#     print(n)
    
age = int(input("Enter the age: "))

if age < 0:
    raise ValueError("Age can't be negative.")

