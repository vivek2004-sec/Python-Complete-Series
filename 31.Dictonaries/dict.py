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
print(vue)

# Access of values based on keys:
print(vue["name"])
print(vue["middle-name"])
print(vue["last-name"])
print(vue["city"])
print(vue["department"])

print(vue.get("name"))
print(vue.get("last-name"))


# Adding new Items in dictionary:
ls = {1:"apple", 2:"mango", 3:"orange"}

ls[4] = "Grapes"
print(ls)

# Updating an existing value:

ls[1] = "watermelon"
print(ls)

# Removing Dictionary Items:

ls = {1:"apple", 2:"mango", 3:"orange", 4: "grapes", 5: "kiwi", 6:"banana"}
del ls[1]
print(ls)
# del: removes an item using its key

print(ls.pop(2))
# pop(): removes the item with the given key and returns its value

d = {"name": "Vivek", "age": 21, "city": "Kolhapur"}

result = d.popitem()

print(result)  # ('city', 'Kolhapur')
print(d)       # {'name': 'Vivek', 'age': 21}
# It removes and returns the last inserted key-value pair as a tuple

print(d.clear())
# Removes all items from dictionary.


# Iterating Through a Dictionary