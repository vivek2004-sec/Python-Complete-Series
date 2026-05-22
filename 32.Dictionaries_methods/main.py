vue = {
    "name": "Vivek",
    "middle-name": "Ranjit",
    "last-name": "Kamble",
    "city": "kagal",
    "department": "CSE",
    "year-of-study": "3rd", 
    "subject": ['maths', 'physics', 'computer networks', 'csi'],
    "marks": (90, 89, 88),
    "group": {"amey", "vivek"},
    "info": {"vivek":"captain", "amey": "vice-captain"}
    
    
    
}



print(vue.keys())
print(list(vue.keys()))
print(vue.values())
print(vue.items())
print(vue.get("subject"))
vue.update({"last-name": "kagale", "department": "it", "standard": "undergraduate"})
print(vue)
print(vue.pop("city"))


d  = {"name": "Vivek", "age": 21}
d2 = d.copy()

d2["name"] = "Kamble"   # changes only d2

print(d)   # {'name': 'Vivek', 'age': 21}   ← original unchanged
print(d2)  # {'name': 'Kamble', 'age': 21}

d = {"name": "vivek", "age": 21}

print(d.setdefault("name", "Unknown"))   # Vivek   ← key exists
print(d.setdefault("city", "Kolhapur"))  # Kolhapur ← key added

print(d)  # {'name': 'Vivek', 'age': 21, 'city': 'Kolhapur'}

d = {"name": "vivek", "age": 21}

d2 = d.fromkeys("keys","unknown" )
print(d2)

# we can get total number of keys.
print(len(d))

for key, value in vue.items():
    print(f"{key}:{value}")