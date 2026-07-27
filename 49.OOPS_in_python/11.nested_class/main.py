
# class Company:
#     class Employee:
#         print("this is the first company.")
    
# class NonProfit:  
#     class Employee:
#         print("this is the second company.")



class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
    
        def get_detail(self):
             return f"{self.name} {self.position}"
    
    
    def __init__(self, company_name):
            self.company_name = company_name
            self.employees = []
            
        
    def add_employee(self, name, position):
            new_employee = self.Employee(name, position)
            self.employees.append(new_employee)
            
    def list_employees(self):
            return [employee.get_detail() for employee in self.employees]
        
company = Company("Microsoft")
company.add_employee("vivek", "SDE II")
company.add_employee("rishi", "SDE II")
company.add_employee("vikrant", "SDE II")

print(company.list_employees())

for employee in company.list_employees():
    print(employee)
    
    
class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        
    class Student:
        def __init__(self, name, standard):
            self.name = name
            self.standard = standard
            
        
        def get_student_details(self):
            return f"{self.name}:{self.standard}"
        
        
    def add_students(self, name, standard):
        new_student = self.Student(name, standard)
        self.students.append(new_student)
        
        
    def list_student(self):
        return [student.get_student_details() for student in self.students]
        
        
school= School(school_name="Shraddha Modern School")
print(school.school_name)

school.add_students(name="vivek", standard= 10)
school.add_students(name="sujal", standard= 10)
school.add_students(name="sahil", standard= 10)
school.add_students(name="sushant", standard= 10)
school.add_students(name="samarth", standard= 10)
school.add_students(name="sai", standard= 10)
print(school.list_student())

for student in school.list_student():
    print(student)