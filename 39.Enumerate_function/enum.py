# The enumerate() function in Python is used to iterate over an iterable while keeping track of both the index and the value.

marks = [60, 56, 45, 55, 67, 23]
for index, mark in enumerate(marks, start = 2):
    print(index, mark)
for index, mark in enumerate(marks):
    print(mark, 'Well Done!') if index == 3 else""
    
for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Well Done!")
    
    
students = {
    "std_name": 'Vivek',
    "std_prn": 2068,
    "branch": 'CSE',
    "year": 'Third'
}

# for key, value in enumerate(students):
#     print(key, value)
    
for key, value in students.items():
    print(key, ":",  value)