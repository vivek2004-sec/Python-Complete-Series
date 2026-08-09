import pandas as pd


#  Dataframes = A tabular data structure with row and columns. (2-Dimensional) Similar to an Excel spreadsheet.


data = {
    "Name": ["Ash", "Misty", "Brock"],
    "Age": [12, 12, 12], 
    "Companions": ["pikachu", "togefree", 'Rocky']
}

df = pd.DataFrame(data, index=[1, 2, 3])
print(df)