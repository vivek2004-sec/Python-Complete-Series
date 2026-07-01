class shape():
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


class Circle(shape):
   def __init__(self, color, is_filled, radius):
       super().__init__(color, is_filled)
       self.radius = radius
          
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