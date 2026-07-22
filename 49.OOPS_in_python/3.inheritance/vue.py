# 1. Single Inheritance: 
    
class Animal: # parent
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def eat(self):
        print(f"the {self.name} is eating.")

class Dog(Animal): # child
    pass

dog = Dog("scooby", "friendly")
print(dog.name)
print(dog.type)
dog.eat()


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
    def __init__(self, type):
            
            self.type = type
            
    def eat(self):
        print(f"the {self.name} is eating.")
    
class Dog(Animal):      # parent
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        
    def favorite(self):
        print("he loves to play.")

class Puppy(Dog):       # child
    pass
# Puppy gets everything from both Dog AND Animal!


puppy = Puppy( "golden", "shaggy")
print(puppy.name)
print(puppy.type)

puppy.eat()
puppy.favorite()