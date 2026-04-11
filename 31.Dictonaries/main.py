# dic = {
#     "vivek": "Human being",
#     "spoon": "get",
#     "apple": "fruit",
#     "car": "vehicle",
#     "tree": "plant",
#     "python": "language",
#     "java": "language"
# }

# print(dic["vivek"])
# print(dic["java"])
# print(dic["python"])
# print(dic["car"])
# print(dic["tree"])
# print(dic["apple"])

# students = {
#     "John": 90,
#     "Emma": 85,
#     "Samuel": 67,
#     "eli": 80,
#     "vivek": 95
# }
# for i in students:
#     print(i)

# print(students["vivek"])
# print(students["Emma"])
# print(students["Samuel"])
# print(students["John"])

info = {"Name": "Vivek", "Age": 20, "Course": "Computer Science", "City": "Kagal"}
# print(info)
# print(info.get('City'))
# print(info.get('Age'))
# print(info["Age"])
# print(info.get('Age2'))

# print(info['Course'])
# print(info.get('City'))
# print(info.get('City2'))
# print(info.keys())
# for keys in info.keys():
#     print(f"The value corresponding to the key {keys} is {info[keys]}")

# for values in info.values():
#     print(values)

print(info.items())
for key, value in info.items():
    
    print(f"The value corresponding to the key {key} is {value}")
    