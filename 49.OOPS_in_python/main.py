# Class → Blueprint
class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand      # attribute
        self.color = color      # attribute
        self.speed = speed      # attribute

    def start(self):            # method
        print(f"{self.brand} is starting!")

    def stop(self):             # method
        print(f"{self.brand} is stopping!")

# Object → Real thing
car1 = Car("Toyota", "Red", 120)
car2 = Car("BMW",    "Blue", 200)

print(car1.brand)       # Toyota
print(car2.brand)       # BMW

car1.start()            # Toyota is starting!
car2.stop()             # BMW is stopping!