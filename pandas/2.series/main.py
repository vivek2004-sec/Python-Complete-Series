import pandas as pd 

data = [100, 101, 104]

series = pd.Series(data)
print(series)


names = ['vivek', 'sujal', 'sai', 'sahil', 'sushant', 'samarth']

std = pd.Series(names)
print(std)

students = {
    'vivek': 1.2,
    'sujal': 3.0
}

obj = pd.Series(students)
print(obj)