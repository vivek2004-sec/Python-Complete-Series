class person:
    name = "vivek"
    age = 22
    occupation = "student"
    city = "kagal"
    branch  = "cse"



a = person()
print(a.name)
print(a.age)
print(a.city)
a.name = "shubham"
a.city = "kolhapur"
print(a.name)
print(a.city)


class city:
    def __init__(self, city_name, country, pincode):
        self.city_name = city_name
        self.country = country
        self.pincode = pincode
          
    
a = city("kagal", "India", 416-216)
print(a.city_name)
print(a.country)
print(a.pincode)



class car: 
    def __init__(self, model, year, color, for_sale): 
        '''
        __init__ is a special method in Python that runs automatically when 
         you create an object from a class. It's called the constructor.
        '''
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
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