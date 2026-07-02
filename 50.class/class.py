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


class cup:
    beverage = "tea"
    size = 30
    is_hot = True
    
b = cup()
print(b.beverage)
print(b.size)
print(b.is_hot)
    

class city:
    def __init__(self, city_name, country, pincode):
        self.city_name = city_name
        self.country = country
        self.pincode = pincode
          
    
a = city("kagal", "India", 416-216)
print(a.city_name)
print(a.country)
print(a.pincode)



