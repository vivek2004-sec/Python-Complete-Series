class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
        
        
class Dog(Animal):
    pass


class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()

# Multiple Inheritance:


class Animal:
    def eat(self):
        print("This animal is eating.")
    def sleep(self):
        print("This animal is sleeping.")
class prey(Animal):
    def flee(self):
        print("This animal is fleeing.")

class predator(Animal):
    def hunt(self):
        print("This animal is hunting.")


class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(prey, predator):
    pass

Rabbit = rabbit()
Hawk = hawk()
Fish = fish()

Rabbit.flee()
Rabbit.eat()
Hawk.hunt()
Fish.flee()
Fish.hunt()