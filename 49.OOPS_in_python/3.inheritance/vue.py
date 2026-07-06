# 1. Single Inheritance: 
    
class Animal: # parent
    pass

class Dog(Animal): # child
    pass


# 2. Multiple Inheritance:

class Father:
    def height(self):
        print("6 feet tall")

class Mother:
    def cooking(self):
        print("Good cook")

class Child(Father, Mother):  # inherits from both!
    pass

c = Child()
c.height()    # from Father → 6 feet tall
c.cooking()   # from Mother → Good cook


# 3. Multilevel Inheritance:
class Animal:           # grandparent
    pass

class Dog(Animal):      # parent
    pass

class Puppy(Dog):       # child
    pass
# Puppy gets everything from both Dog AND Animal!