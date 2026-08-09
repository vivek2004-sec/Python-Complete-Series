import pandas as pd

# Data Cleaning : the process of fixing/removing : 
#                 incomplete, incorrect, or irrevelant data.
#                  ~75% of work done with pandas is data cleaning. 

df = pd.read_csv('pandas/8.data_cleaning/pokemon.csv')

# 1. Drop a column
# df = df.drop(columns=["Legendary", 'Height', 'W

# 2. Handle Missing values
# df = df.dropna(subset=["Type1", "Type2"])
# df = df.fillna({"Type2": "NONE"})

# 3. Fix inconsistent values
# df["Type1"] = df['Type1'].replace({"Grass": "GRASS"})

# 4. Standardize Text
# df['Name'] = df['Name'].str.lower()

# 5. changing data types 

# df["Legendary"] = df['Legendary'].astype(bool)
print(df.to_string())