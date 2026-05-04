letter = "hey my name is {}  and I am from {}"
country = "India"
name = "Vivek"

print(letter.format(country, name))
print(f"Hey my name is {name} nad I am from {country}")

txt = f"{77, 33, 55, 33, 55}"
print(txt)
print(type(txt))
for i in txt:
    print(i)
    
    
    
name = 'vivek'
age = 22
intro = f"Hello, my name is {name}, my age is {age}."
print(intro)

import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")


marks = 45
total_marks = 50

info = f"out of 20 students 15 students scored {marks} and 2 students scored {total_marks}"
print(info)