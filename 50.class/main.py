from car import car
        
car1 = car("mustang", 2022, "black", False) # object
car2 = car("corvette", 2024, "blue", True)  # object
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


# Class Variables:

class students:
    
    class_year = 2027
    num_students = 0
    
    def __init__(self, name, age):
        self.age = age
        self.name = name
        students.num_students += 1
        
student1 = students('Spongebob', 20)
student2 = students('Patrick', 20)
student2 = students('Squidward', 40)
student2 = students('Sandy', 27)
student2 = students('Sailor MOon', 17)
print(student1)
print(student1.name)
print(student1.age)
print(students.class_year)
print(student2.name)
print(student2.age)
print(students.class_year)
print(f"My graduating class of {students.num_students}")