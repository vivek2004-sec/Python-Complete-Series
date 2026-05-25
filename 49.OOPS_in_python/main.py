# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

# Child class → inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking!")

# Child class → inherits from Animal
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing!")

dog = Dog("Bruno")
dog.eat()           # Bruno is eating!   ← from Animal
dog.sleep()         # Bruno is sleeping! ← from Animal
dog.bark()          # Bruno is barking!  ← from Dog

cat = Cat("Kitty")
cat.eat()           # Kitty is eating!   ← from Animal
cat.meow()          # Kitty is meowing!  ← from Cat