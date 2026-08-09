import pandas as pd


#  Dataframes = A tabular data structure with row and columns. (2-Dimensional) Similar to an Excel spreadsheet.


# data = {
#     "Name": ["Ash", "Misty", "Brock"],
#     "Age": [12, 12, 12], 
#     "Companions": ["pikachu", "togefree", 'Rocky']
# }

# df = pd.DataFrame(data, index=[1, 2, 3])

# # Add a new column 
# df['job'] = ['Trainer', 'gym master', 'gym master']

# # Add a new row
# new_row = pd.DataFrame({"Name": "Sandy", "Age": 20, "Companions": 'balbasaur', 'job':"trainer"}, index=[4])
# df = pd.concat([df, new_row])
# print(df)


# print(df.loc[3])
# print(df.iloc[0])


students = {
    "name": ['vivek', 'sujal', 'aditya', 'sahil'],
    "age": [22, 22, 22, 22], 
    'branch': ['cse', 'chemical', 'cse', 'civil']
}

df = pd.DataFrame(students, index=[1, 2, 3, 4])
# Adding a column
df['city'] = ['kagal', 'kagal', 'kagal', 'kagal']
# Adding  Rows
new_row = pd.DataFrame([{"name": 'sai', 'age': 22, 'branch': 'commerce', 'city': 'kagal'},
                       {"name": 'sainath', 'age': 22, 'branch': 'commerce', 'city': 'kagal'},
                       {"name": 'sushant', 'age': 22, 'branch': 'bio', 'city': 'kolhapur'}], index=[5, 6, 7])
df = pd.concat([df, new_row])
print(df)