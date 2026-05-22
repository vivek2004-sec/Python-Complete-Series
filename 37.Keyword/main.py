# def func():
    
#  try: 
#     l = [1,2,3,4,5,6]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#  except:
#     print("Invalid index")
#     return 0
#  finally:
#     print("This will run regardless of the exception")
#     # print("This will run regardless of the exception")

# x = func()
# print(x)

# try:
   
#    l = [1,2, 3, 4]

#    print(len(l))
#    i = int(input("Enter the index: "))
#    print(l[i])
# except IndexError:
#    print("Index is not correct.")
   
# finally:
#    print("I am always executed.")
   
   
try:
   n = int(input("Enter the num: "))
   s = n/0
except ZeroDivisionError:
  print("We can't divide something with zero.")

finally: 
   print("the code is finished.")