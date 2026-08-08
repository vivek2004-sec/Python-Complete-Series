import pandas as pd 


#  For list
data = [100, 101, 104]

series = pd.Series(data, index=['a', 'b', 'c'])
print(series)
print(series.loc['a']) # loc = location by label
print(series.loc['c']) # loc = location by label
series.loc['c'] = 200
print(series)

# # For list 
# names = ['vivek', 'sujal', 'sai', 'sahil', 'sushant', 'samarth']

# std = pd.Series(names)
# print(std)


# # For dictionary
# students = {
#     'vivek': 1.2,
#     'sujal': 3.0
# }

# obj = pd.Series(students)
# print(obj)

# For tuple
fruits = ('apple', 'mango', 'grapes', 'banana')

shakes = pd.Series(fruits)
print(shakes.loc[0])