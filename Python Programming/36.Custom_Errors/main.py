# a = int(input("Enter any value between 5 and 9: "))
# if a >= 5 or a <= 9:
#     raise ValueError ("value should be between 5 and 9")


vue = [1,23,4,55,56,45,33]
i = int(input("Enter the num: "))
print(vue[i])
if i == len(vue):
 raise IndexError ("Index is not correct.")

