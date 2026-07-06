from abc import ABC, abstractmethod


class shape:
    
    @abstractmethod
    def area(self):
        pass
    
    
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.1 * self.radius ** 2

class Square(shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
       return 0.5 * self.base * self.height


shapes = [Circle(3), Square(5), Triangle(7, 9)]

for shape in shapes:
    print(f"{shape.area()} cm²")