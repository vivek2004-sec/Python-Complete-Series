class Student:
    count = 0
    
    def __init__(self, std_name, age):
        self.std_name = std_name
        self.age = age
        Student.count += 1
    
    #Instance Methods
    def get_info(self):
        return f"{self.std_name}:{self.age}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    

student1 = Student("bob", 22)
student2 = Student("max", 22)
student3 = Student("cassey", 22)
student4 = Student("brian", 22)
print(Student.get_count())


        