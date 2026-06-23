def add(a: int, b: int) -> int:
    
    return a + b


def subtract(a: int, b: int) -> int:
    
    return a - b

print("This is simple Calculator!")
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
print(f"The sum is: {add(num1, num2)}")
print(f"The difference  is: {subtract(num1, num2)}")


    