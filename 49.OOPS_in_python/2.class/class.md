Class :

A class is a collection of objects. Classes are blueprints for creating objects.
A class defines a set of attributes and methods that the created objects (instances) can have.

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator.

# class variables :

shared among all instances of class defined outside the constructor allow you to share all data among the objects
created from that class.
It's good to access the class variable by it's own class.

class car:
def **int**(self, model, year, color, for_sale): # method
self.model = model
self.year = year
self.color = color
self.for_sale = for_sale

car1 = car("mustang", 2022, "black", False)
print(car1)
Jul 1
Your code has a bug — **int** should be **init**:

python
class Car:
def **init**(self, model, year, color, for_sale): # ✅ **init** not **int**
self.model = model
self.year = year
self.color = color
self.for_sale = for_sale

car1 = Car("Mustang", 2022, "Black", False)
print(car1.model) # Mustang
print(car1.year) # 2022
print(car1.color) # Black
print(car1.for_sale) # False
Two mistakes fixed:

1 — **int** → **init**
**init** is the constructor method that runs automatically when you create an object. **int** is something completely different — it converts an object to an integer.

2 — class car → class Car
Python convention says class names should always be CapitalCase (called PascalCase). Not required but strongly recommended.

Also — print(car1) prints the object memory address:

<**main**.Car object at 0x000001A2B3C4>
That's why you need print(car1.model) to see actual values.

To make print(car1) show useful info, add **str**:

python
def **str**(self):
return f"{self.year} {self.color} {self.model} - For Sale: {self.for_sale}"

print(car1) # 2022 Black Mustang - For Sale: False
Want me to explain classes and objects in more detail?

# what is (**init**)?

What is **init**?
**init** is a special method in Python that runs automatically when you create an object from a class.
It's called the constructor.

# What is self?

self refers to the current object being created. It's how the object refers to itself.
