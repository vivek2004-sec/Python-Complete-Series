# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is ")

# try:
#     for i in range (1, 11):
#        print(f"{int(a)} X {i} = {int(a) * i}")

# except Exception as e:
#     print("Invalid Input.")

# print("some lines of code.")
# print("End of program.")

# try:
#     num = int(input("Enter the integer: "))
# except ValueError:
#     print("Number entered is not an integer.")
    
try:
    num = int(input("Enter the digit: "))
    a = [6, 3, 7, 5, 6, 8, 99]
    print(a[num])
except ValueError:
    print("the entered is not an integer.")  
except IndexError:
    print("Index Error")


