class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("Woof!")
    
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
class Car:
    
    alive = False
    def speak(self):
        print("Honk!")
        
        
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
    
    
    
    
# Example:

class human:
    def eat(self):
        print("you can eat.")
        
        
class vivek(human):
    def gender(self):
        print("male")

        
        
class tanvi(human):
    def gender(self):
        print("female")


class robot:
    def gender(self):
        print("not specified!")


peoples = [vivek(), tanvi(), robot()]

for i in peoples:
    i.gender()