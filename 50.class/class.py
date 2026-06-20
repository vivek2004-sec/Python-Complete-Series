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