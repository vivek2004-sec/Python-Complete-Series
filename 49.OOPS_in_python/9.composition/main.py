# class Engine:
#     def __init__(self):
#         self.status = "running"

# class Car:
#     def __init__(self):
#         self.engine = Engine()   # Car creates its own Engine internally

# car = Car()
# del car   # when car is destroyed, its engine goes with it — no external reference


# class Engine:
#     def __init__(self, horse_power):
#         self.horse_power = horse_power

# class Wheel:
#    def __init__(self, size):
#        self.size = size

# class Car:
#     def __init__(self, make, model, horse_power, wheel_size):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [Wheel(wheel_size) for wheel in range(4)]
        

# car = Car(make="Ford", model="Mustang", )


import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print("\n", calendar.month(year, month))