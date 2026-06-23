def add(a: int, b: int) -> int:
    
    return a + b


def subtract(a: int, b: int) -> int:
    
    return a - b


if __name__== "__main__":
    print("This is simple Calculator!")
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    print(f"The sum is: {add(num1, num2)}")
    print(f"The difference  is: {subtract(num1, num2)}")

print(__name__)
    
    
# multiplication = lambda a,b : a*b

def multiplication(a,b):
    return a*b

if __name__ == "__main__":
    print(multiplication(8,9))