# single Inheritance:

class vehicle:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
        
    def drive(self):
        print("You can drive.")
        
    def stop(self):
        print("You can stop.")
        
        
bike = vehicle("kawasaki", 200)
print(bike)
print(bike.name)
print(bike.hp)
bike.drive()