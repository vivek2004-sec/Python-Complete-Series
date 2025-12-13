# Strings are immutable 
import string
a= "!!vivek!!! !!!! vivek"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.strip("!"))
print(a.replace("vivek","sujal"))
print(a.replace("vivek","vikrant"))
print(a.split()) # creates list of the given string
cleaned = a.translate(str.maketrans('','', string.punctuation))
print(cleaned)


blogheading = "introduction tO vivek Kambles website js."()
print(blogheading.capitalize())

str1 = "Welcome to the Console !!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50))) #center function adds more length to the string just to place it in the centre.
print(a.count("vivek"))
print(str1.endswith("!!!"))
print(str1.endswith("!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith('to', 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())

str1 = "Welcome00"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "HELLO WORLD"
print(str1.isupper())

str1 = "We wish you a merry christmas."
print(str1.isprintable())