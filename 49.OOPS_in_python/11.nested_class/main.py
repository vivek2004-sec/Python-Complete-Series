
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