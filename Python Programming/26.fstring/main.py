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
