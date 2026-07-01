# Inheritance :

Allows a class to inherit attributes and methods from another class.
Helps with code reusability and extensibility.
class child(Parent)

# Types of Inheritance:

1. Single Inheritance
   One child, One parent.

class Animal: # parent
pass

class Dog(Animal): # child
pass

2. Multiple Inheritance
   inherit from more than one parent class
   c(A,B)
   class Father:
   def height(self):
   print("6 feet tall")

class Mother:
def cooking(self):
print("Good cook")

class Child(Father, Mother): # inherits from both!
pass

c = Child()
c.height() # from Father → 6 feet tall
c.cooking() # from Mother → Good cook
