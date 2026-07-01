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
    
    def __init__(self, name):
         self.name = name
     
    def eat(self):
        print(f"This {self.name} is eating.")
        
    def sleep(self):
        print(f"This {self.name} is sleeping.")
        
        
class prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing.")

class predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting.")


class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(prey, predator):
    pass

Rabbit = rabbit("Bugs")
Hawk = hawk("Tony")
Fish = fish("Nemo")

Rabbit.flee()
Rabbit.eat()
Hawk.hunt()
Fish.flee()
Fish.hunt()