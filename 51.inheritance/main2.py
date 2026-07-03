class school:
    def __init__(self, school_name, city):
        self.school_name = school_name
        self.city = city    
class classroom(school):
    def classroom(self ):
        print("std: 10")
        print("total_student: 50")       
class student(school):
    def name(self):
        print("name: vivek")
        print("age: 20")
class boy(classroom, student):
    pass

b = boy("SMS", "kagal")
print(b)