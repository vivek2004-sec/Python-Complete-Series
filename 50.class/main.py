from car import car
        
car1 = car("mustang", 2022, "black", False)
car2 = car("corvette", 2024, "blue", True)
print(car1)
print(car1.model) # (.) is know attribute access operator.
print(car1.color) 
print(car1.year) 
print(car1.for_sale) 
print(car2.model) 
print(car2.color) 
print(car2.year) 
print(car2.for_sale) 

car1.drive()
car1.stop()
car2.drive()
car2.stop()
car2.describe()