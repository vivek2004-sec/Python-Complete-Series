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
    city_name = "Kagal"
    district = 'Kolhapur'
    state = "Maharashtra"
    country = "India"
    pin_code = 416-216
    
a = city()
print(a.city_name)
a.city_name = "Pimpalgaon"
print(a.city_name)
a.country = "USA"
print(a.country)


class car: 
    def __init__(self, model, year, color, for_sale): # __init__ is a special method in Python that runs automatically when 
        # you create an object from a class. It's called the constructor.
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
car1 = car("mustang", 2022, "black", False)
print(car1)
print(car1.model) # (.) is know attribute access operator.