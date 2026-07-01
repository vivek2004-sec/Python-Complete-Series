class shape():
    pass


class Circle(shape):
   def __init__(self, color, is_filled, radius):
       self.color = color
       self.is_filled = is_filled
       self.radius = radius
          
class Square(shape): 
    def __init__(self, color, is_filled, width):
        self.color = color
        self.is_filled = is_filled
        self.width = width

class Triangle(shape):
    def __init__(self, color, is_filled, width, height):
        self.color = color
        self.is_filled = is_filled
        self.width = width
        self.height = height