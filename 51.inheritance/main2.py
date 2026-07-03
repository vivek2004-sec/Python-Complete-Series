class school:
    def school(self, school_name, city):
        self.school_name = school_name
        self.city = city    
class classroom:
    def classroom(self, std, total ):
        self.std = std
        self.total = total
        
class student(school, classroom):
    def __init__(self, name, age):
        self.name = name
        self.age = age

boy = student(school_name = "SMS", city = "kagal", std = 10, total = 30, name= "vivek", age=22 )
print(boy)