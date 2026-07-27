class cal:
    @staticmethod
    def add(a, b):
        return a + b

        """In this example we didn't defined any self attributes.
        not also used __init__ constructor.
        """
sum = cal.add(3, 4)
print(sum)

'''
@staticmethod makes add() independent of class object.
We directly called the add() method using the class name.
'''
class Check:
    @staticmethod
    def is_even(n):
        return n % 2 == 0
    
    
    def find(is_even):
        if is_even == True:
                print("The number is even.")
        else:
            print("The number is odd.")

print(Check.is_even(9))
Check.find()