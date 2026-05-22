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
    
# try:
#     num = int(input("Enter the digit: "))
#     a = [6, 3, 7, 5, 6, 8, 99]
#     print(a[num])
# except ValueError:
#     print("the entered is not an integer.")  
# except IndexError:
#     print("Index Error")


# n = 5
# m = 0

# try:
#     div = n /m
    
# except ZeroDivisionError:
#     print("Can't be divided by zero!.")

# num = input("Enter the number: ")
# try:
#     for i in range(1, 11):
#         print(f"{int(num)} X {i} = {int(num)*i}")
# except:
#     print("Sorry some error occured.")
 
# else:      
#   print(f"this is the table of {num}.")




# def mean(a,b):
#     mean = a +b / 2
#     print(mean)
 
# try:  
#   a = (input("enter the number."))
#   b = input("enter the number.")
#   mean(a,b)

# except:
#     print("Sorry an error has occured.")


try:
    n = 0
    res = 100/n

except ZeroDivisionError:
    print("You can't divide by zero.")

except ValueError:
    print("enter the correct value.")

else:
    print("error has occured.")

finally:
    print("The program is complete.")
    
    
    
try:
    n = 0
    m = int(input("Enter the num: "))
    product = n*m
except:
    print("the value is zero.")
else:
    print("The final answer.")
finally:
    print("The output.")