def func():
    
 try: 
    l = [1,2,3,4,5,6]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
 except:
    print("Invalid index")
    return 0
 finally:
    print("This will run regardless of the exception")
    # print("This will run regardless of the exception")

x = func()
print(x)