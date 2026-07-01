class shape():
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled."}")


class Circle(shape):
   def __init__(self, color, is_filled, radius):
       super().__init__(color, is_filled)
       self.radius = radius
       
   def describe(self):
        print(f"The area of the circle is {3.14 * self.radius * self.radius}cm^2") # Method Overriding.
          
class Square(shape): 
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        
        
circle = Circle("red", True, 5)
square = Square("White", True, 7)
print(circle.color)
print(circle.is_filled)
print(square.color)
print(square.is_filled)

circle.describe()
square.describe()