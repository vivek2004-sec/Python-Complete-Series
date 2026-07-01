from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod 
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    
class Car(Vehicle):
    
    def go(self):
        print("You drive the car.")
        
    def stop(self):
        print("You stop the car.")
    
class Motorcycle(Vehicle):
    def __init__(self, name):
        self.name = name
    
    def go(self):
        print("You ride the motorcycle.")
        
    def stop(self):
        print("You stop the motorcycle.")
    
    
motorcycle = Motorcycle("Bullet")
print(motorcycle.name)
motorcycle.go()
motorcycle.stop()


class Boat(Vehicle):
    def go(self):
        print("You ride the boat.")
        
    def stop(self):
        print("You stop the boat.")

boat = Boat()
    